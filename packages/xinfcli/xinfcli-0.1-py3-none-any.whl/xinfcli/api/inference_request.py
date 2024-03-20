from abc import ABC, abstractmethod
from typing import Any, cast, Dict, List, Optional, Tuple, Union

from numpy import ndarray, nditer, object_ as np_dtype_object

from xinfcli.model_utils import serialize_bytes_tensor, TensorDataType
from xinfcli.utils import client_logger

# https://github.com/triton-inference-server/tutorials/blob/main/Quick_Deploy/PyTorch/client.py


class InferenceRequestIOItem(ABC):
    _name: str
    _is_binary_data: bool
    _parameters: Dict[str, Any]

    def __init__(self, name: str, is_binary_data: bool = True):
        self._name = name
        self._is_binary_data = is_binary_data
        self._parameters = {}

    @abstractmethod
    def serialize_to_json(self) -> Dict[str, Any]:
        pass

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_binary_data(self) -> bool:
        return self._is_binary_data


class InferenceRequestInputItem(InferenceRequestIOItem):
    __shape: Union[List[int], Tuple[int, ...]]
    __data_type: TensorDataType
    __non_binary_data: Optional[List[Any]]
    __binary_data: Optional[bytes]

    def __init__(
        self,
        name: str,
        shape: Union[List[int], Tuple[int, ...]],
        data_type: TensorDataType,
    ):
        super().__init__(name, False)
        self.__shape = shape
        self.__data_type = data_type
        self.__non_binary_data = None
        self.__binary_data = None

    @property
    def binary_data(self) -> Optional[bytes]:
        return self.__binary_data

    def set_data(self, input_tensor: ndarray, is_binary_data: bool):
        self._is_binary_data = is_binary_data
        is_shape_valid: bool = True

        if len(input_tensor.shape) != len(self.__shape):
            is_shape_valid = False
        else:
            for i in range(len(input_tensor.shape)):
                if input_tensor.shape[i] != self.__shape[i]:
                    is_shape_valid = False
                    break

        if not is_shape_valid:
            self._is_binary_data = False
            self.__non_binary_data = None
            self.__binary_data = None
            self._parameters.pop("binary_data_size", None)
            client_logger.info(
                f"Input shape {input_tensor.shape} does not match expected shape {self.__shape}."
            )
            return

        try:
            if self.is_binary_data:
                self.__non_binary_data = None

                if self.__data_type == TensorDataType.TYPE_BYTES:
                    serialized_output = serialize_bytes_tensor(input_tensor)

                    if serialized_output.size > 0:
                        self.__binary_data = serialized_output.item()
                    else:
                        self.__binary_data = b""
                else:
                    self.__binary_data = input_tensor.tobytes()

                self._parameters["binary_data_size"] = len(self.__binary_data)
            else:
                self.__binary_data = None
                self._parameters.pop("binary_data_size", None)

                if self.__data_type == TensorDataType.TYPE_BYTES:
                    self.__non_binary_data = []

                    if input_tensor.size > 0:
                        for value in nditer(input_tensor, flags=["refs_ok"], order="C"):
                            value = cast(ndarray, value)

                            if input_tensor.dtype == np_dtype_object:
                                if type(value[0].item()) == bytes:
                                    self.__non_binary_data.append(
                                        str(value.item(), encoding="utf-8")
                                    )
                                else:
                                    self.__non_binary_data.append(str(value.item()))
                            else:
                                self.__non_binary_data.append(
                                    str(value.item(), encoding="utf-8")
                                )
                else:
                    self.__non_binary_data = [
                        value.item() for value in input_tensor.flatten()
                    ]
        except Exception as e:
            client_logger.error(f"Exception occurred.\n[Exception] {e}")
            self._is_binary_data = False
            self.__non_binary_data = None
            self.__binary_data = None
            self._parameters.pop("binary_data_size", None)

    def __get_mapping_data_type(self) -> str:
        return self.__data_type.value.replace("TYPE_", "")

    def serialize_to_json(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {
            "name": self.name,
            "shape": self.__shape,
            "datatype": self.__get_mapping_data_type(),
        }

        if not self.is_binary_data and self.__non_binary_data is not None:
            result["data"] = self.__non_binary_data

        if self._parameters:
            result["parameters"] = self._parameters

        return result


class InferenceRequestOutputItem(InferenceRequestIOItem):
    def __init__(self, name: str, *, is_binary_data: bool = True, class_count: int = 0):
        super().__init__(name, is_binary_data)
        self._parameters["binary_data"] = self.is_binary_data

        if class_count != 0:
            self._parameters["classification"] = class_count

    def serialize_to_json(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "parameters": self._parameters,
        }
