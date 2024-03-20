from struct import pack, unpack_from
from typing import cast, List

from numpy import (
    array as np_array,
    ascontiguousarray,
    asarray,
    bytes_ as np_dtype_bytes,
    empty as np_empty,
    ndarray,
    nditer,
    object_ as np_dtype_object,
)

from xinfcli.utils import client_logger


def serialize_bytes_tensor(input_tensor: ndarray) -> ndarray:
    """
    Parameters:
        input_tensor: input tensor where each item is bytes
    Returns:
        np.ndarray: the serialized tensor, which is a flat array, each item is string
    """
    result: ndarray = np_array([])

    try:
        if input_tensor.size == 0:
            return np_empty([0], dtype=np_dtype_object)

        if (input_tensor.dtype != np_dtype_object) and (
            input_tensor.dtype.type != np_dtype_bytes
        ):
            return np_array([])

        flattened_list = []

        for value in nditer(input_tensor, flags=["refs_ok"], order="C"):
            value = cast(ndarray, value)
            tmp_bytes: bytes = b""

            if input_tensor.dtype == np_dtype_object:
                if type(value.item()) == bytes:
                    tmp_bytes = value.item()
                else:
                    tmp_bytes = str(value.item()).encode("utf-8")
            else:
                tmp_bytes = value.item()

            flattened_list.append(pack("<I", len(tmp_bytes)))
            flattened_list.append(tmp_bytes)

        result = asarray(b"".join(flattened_list), dtype=np_dtype_object)

        if not result.flags["C_CONTIGUOUS"]:
            result = ascontiguousarray(result, dtype=np_dtype_object)
    except Exception as e:
        client_logger.error(f"Exception occurred.\n[Exception] {e}")

    return result


def deserialize_bytes_to_tensor(raw_data: bytes) -> ndarray:
    """
    Parameters:
        raw_data: the serialized tensor, which is a flat array, each item has 2 parts: length in first 4 bytes and content followed by
    Returns:
        ndarray: output tensor where each item is deserialized bytes
    """

    interm_list: List[bytes] = []
    cur_offset: int = 0
    try:
        while cur_offset < len(raw_data):
            item_length = unpack_from("<I", raw_data, cur_offset)[0]
            cur_offset += 4
            item_content: bytes = unpack_from(
                "<{}s".format(item_length), raw_data, cur_offset
            )[0]
            cur_offset += item_length
            interm_list.append(item_content)
    except Exception as e:
        client_logger.error(f"Exception occurred.\n[Exception] {e}")

    return np_array(interm_list, dtype=np_dtype_object)
