from gzip import decompress as gzip_decompress
from json import loads
from typing import Any, cast, Dict, List, Optional, Type, TypedDict
from zlib import decompress as zlib_decompress

from numpy import (
    array as np_array,
    empty as np_empty,
    float16 as np_dtype_float16,
    float32 as np_dtype_float32,
    float64 as np_dtype_float64,
    frombuffer,
    int16 as np_dtype_int16,
    int32 as np_dtype_int32,
    int64 as np_dtype_int64,
    int8 as np_dtype_int8,
    ndarray,
    object_ as np_dtype_object,
    uint16 as np_dtype_uint16,
    uint32 as np_dtype_uint32,
    uint64 as np_dtype_uint64,
    uint8 as np_dtype_uint8,
)

from xinfcli.model_utils import deserialize_bytes_to_tensor
from xinfcli.utils import client_logger


class InferenceResponseOutputItemParameters(TypedDict):
    binary_data_size: Optional[int]


class InferenceResponseOutputItem(TypedDict):
    name: str
    datatype: str
    shape: List[int]
    data: Optional[List[Any]]
    parameters: Optional[InferenceResponseOutputItemParameters]


class InferenceResponseJSON(TypedDict):
    model_name: str
    model_version: str
    outputs: List[InferenceResponseOutputItem]


class DecompressedResponse:
    __data: bytes
    __offset: int

    def __init__(self, data: bytes):
        self.__data = data
        self.__offset = 0

    def read(self, length: int = -1):
        if length < 0:
            return self.__data[self.__offset :]
        else:
            prev_offset = self.__offset
            self.__offset += length
            return self.__data[prev_offset : self.__offset]


def is_data_compressed(data: bytes) -> bool:
    if len(data) < 2:
        return False

    return (
        data.startswith(b"\x1f\x8b")
        or data.startswith(b"\x78\x9c")
        or data.startswith(b"\x78\xda")
    )


def convert_to_np_dtype(raw_type: str) -> Optional[Type]:
    if raw_type == "BOOL":
        return bool
    elif raw_type == "INT8":
        return np_dtype_int8
    elif raw_type == "INT16":
        return np_dtype_int16
    elif raw_type == "INT32":
        return np_dtype_int32
    elif raw_type == "INT64":
        return np_dtype_int64
    elif raw_type == "UINT8":
        return np_dtype_uint8
    elif raw_type == "UINT16":
        return np_dtype_uint16
    elif raw_type == "UINT32":
        return np_dtype_uint32
    elif raw_type == "UINT64":
        return np_dtype_uint64
    elif raw_type == "FP16":
        return np_dtype_float16
    elif raw_type == "FP32":
        return np_dtype_float32
    elif raw_type == "FP64":
        return np_dtype_float64
    elif raw_type == "BYTES":
        return np_dtype_object

    return None


class InferenceResponse:
    __json: Optional[InferenceResponseJSON]
    __buffer: bytes
    __name_to_buffer_index_map: Dict[str, int]

    def __init__(
        self,
        response_payload: bytes,
        inference_header_content_length: Optional[str],
        content_encoding: Optional[str],
    ):
        self.__json = None
        self.__buffer = b""
        self.__name_to_buffer_index_map = {}
        decompressed_response = DecompressedResponse(b"")

        if content_encoding is not None and is_data_compressed(response_payload):
            if content_encoding == "gzip":
                decompressed_response = DecompressedResponse(
                    gzip_decompress(response_payload)
                )
            elif content_encoding == "deflate":
                decompressed_response = DecompressedResponse(
                    zlib_decompress(response_payload)
                )
        else:
            decompressed_response = DecompressedResponse(response_payload)

        try:
            if inference_header_content_length is None:
                self.__json = cast(
                    InferenceResponseJSON, loads(decompressed_response.read())
                )
            else:
                self.__json = cast(
                    InferenceResponseJSON,
                    loads(
                        decompressed_response.read(int(inference_header_content_length))
                    ),
                )
                self.__buffer = decompressed_response.read()
                buffer_index: int = 0

                for output_item in self.__json["outputs"]:
                    if "parameters" not in output_item:
                        continue

                    parameters = cast(
                        InferenceResponseOutputItemParameters,
                        output_item["parameters"],
                    )

                    if "binary_data_size" not in parameters:
                        continue

                    cur_data_size = cast(int, parameters["binary_data_size"])
                    self.__name_to_buffer_index_map[output_item["name"]] = buffer_index
                    buffer_index += cur_data_size
        except Exception as e:
            client_logger.error(
                f"Exception occurred when parsing inference response.\n[Exception] {e}"
            )

    def get_output(self, name: str) -> ndarray:
        output: ndarray = np_empty(0)

        try:
            if self.__json is None:
                return output

            for output_item in self.__json["outputs"]:
                if output_item["name"] != name:
                    continue

                data_type = output_item["datatype"]
                is_binary_data: bool = False

                if "parameters" in output_item:
                    parameters = cast(
                        InferenceResponseOutputItemParameters,
                        output_item["parameters"],
                    )

                    if "binary_data_size" not in parameters:
                        break

                    cur_data_size = cast(int, parameters["binary_data_size"])
                    is_binary_data = True

                    if cur_data_size < 0 or name not in self.__name_to_buffer_index_map:
                        break

                    start_index = self.__name_to_buffer_index_map[name]
                    end_index = start_index + cur_data_size
                    if data_type == "BYTES":
                        output = deserialize_bytes_to_tensor(
                            self.__buffer[start_index:end_index]
                        )
                    else:
                        output = frombuffer(
                            self.__buffer[start_index:end_index],
                            convert_to_np_dtype(data_type),
                        )

                if not is_binary_data and "data" in output_item:
                    output = np_array(
                        output_item["data"], dtype=convert_to_np_dtype(data_type)
                    )

                output = cast(ndarray, output.reshape(output_item["shape"]))
                break
        except Exception as e:
            client_logger.error(
                f"Exception occurred when parsing inference response.\n[Exception] {e}"
            )

        return output
