from abc import ABC
from typing import Any, Dict, List, Optional, Sequence

from .data_type import TensorDataType
from xinfcli.utils import client_logger, PbtxtParser, PbtxtValue

# TODO: Rate Limiter options
# https://github.com/triton-inference-server/server/blob/main/docs/user_guide/model_configuration.md


class ModelConfigIOItem(ABC):
    _name: str
    _data_type: TensorDataType
    _dims: List[int]
    _reshape: Optional[List[int]]

    def __init__(
        self,
        name: str,
        data_type: TensorDataType,
        dims: List[int],
        *,
        reshape: Optional[List[int]] = None,
    ):
        self._name = name
        self._data_type = data_type
        self._dims = dims
        self._reshape = reshape if reshape else None

    @property
    def name(self) -> str:
        return self._name

    @property
    def data_type(self) -> TensorDataType:
        return self._data_type

    @property
    def dims(self) -> List[int]:
        return self._dims

    @property
    def reshape(self) -> Optional[List[int]]:
        return self._reshape


class ModelConfigInputItem(ModelConfigIOItem):
    def __init__(
        self,
        name: str,
        data_type: TensorDataType,
        dims: List[int],
        *,
        reshape: Optional[List[int]] = None,
    ):
        super().__init__(name, data_type, dims, reshape=reshape)


class ModelConfigOutputItem(ModelConfigIOItem):
    def __init__(
        self,
        name: str,
        data_type: TensorDataType,
        dims: List[int],
        *,
        reshape: Optional[List[int]] = None,
    ):
        super().__init__(name, data_type, dims, reshape=reshape)


class ModelConfig:
    __name: str
    __platform: str
    __max_batch_size: int
    __input: List[ModelConfigInputItem]
    __output: List[ModelConfigOutputItem]

    def __init__(
        self,
        name: str,
        *,
        platform: str = "pytorch_libtorch",
        max_batch_size: int = 0,
    ):
        self.__name = name
        self.__platform = platform
        self.__max_batch_size = max_batch_size
        self.__input = []
        self.__output = []

    def add_input(
        self,
        name: str,
        data_type: TensorDataType,
        dims: List[int],
        *,
        reshape: Optional[List[int]] = None,
    ):
        self.__input.append(
            ModelConfigInputItem(name, data_type, dims, reshape=reshape)
        )

    def add_output(
        self,
        name: str,
        data_type: TensorDataType,
        dims: List[int],
        *,
        reshape: Optional[List[int]] = None,
    ):
        self.__output.append(
            ModelConfigOutputItem(name, data_type, dims, reshape=reshape)
        )

    def serialize_to_pbtxt(self) -> str:
        def format_io_item(
            item_list: Sequence[ModelConfigIOItem], indent_layer: int, indent_size: int
        ) -> str:
            new_line = "\n"
            item_delimiter = ","

            return f"""{
    item_delimiter.join(formatted_item for formatted_item in list(map( lambda item: f'''
{' ' * indent_layer * indent_size}{{
{' ' * (indent_layer + 1) * indent_size}name: "{item.name}"
{' ' * (indent_layer + 1) * indent_size}data_type: {item.data_type.value}
{' ' * (indent_layer + 1) * indent_size}dims: [ {', '.join(str(value) for value in item.dims)} ]{
        f"{new_line}{' ' * (indent_layer + 1) * indent_size}reshape {{ shape: [ {', '.join(str(value) for value in item.reshape)} ] }}" if item.reshape is not None else ""}
{' ' * indent_layer * indent_size}}}''', item_list)))
}"""

        return f"""
name: "{self.__name}"
platform: "{self.__platform}"
max_batch_size: {self.__max_batch_size}
input [{ format_io_item(self.__input, 1, 2) }
]
output [{ format_io_item(self.__output, 1, 2) }
]
"""

    def serialize_to_json(self) -> Dict[str, Any]:
        def format_io_item(item_list: Sequence[ModelConfigIOItem]) -> List[Any]:
            result: List[Any] = []
            for item in item_list:
                tmp_item = {
                    "name": item.name,
                    "data_type": item.data_type.value,
                    "dims": item.dims,
                }

                if item.reshape is not None:
                    tmp_item["reshape"] = {"shape": item.reshape}

                result.append(tmp_item)

            return result

        return {
            "name": self.__name,
            "platform": self.__platform,
            "max_batch_size": self.__max_batch_size,
            "input": format_io_item(self.__input),
            "output": format_io_item(self.__output),
        }

    @staticmethod
    def init_from_file(path: str) -> Optional["ModelConfig"]:
        def add_inputs(_config: ModelConfig, _value: Optional[PbtxtValue]):
            if _value is None:
                return

            for input_item in _value.get_list():
                input_item_object = input_item.get_object()

                if (
                    "name" not in input_item_object
                    or "data_type" not in input_item_object
                    or "dims" not in input_item_object
                ):
                    continue

                _name = input_item_object["name"].get_string()
                _data_type = input_item_object["data_type"].get_identifier()
                _dims: List[int] = []
                _reshape: List[int] = []

                if _name is None or _data_type is None:
                    continue

                for dim_value in input_item_object["dims"].get_list():
                    tmp_dim = dim_value.get_int()

                    if tmp_dim is not None:
                        _dims.append(tmp_dim)

                if "reshape" in input_item_object:
                    reshape_object = input_item_object["reshape"].get_object()

                    if "shape" in reshape_object:
                        for reshape_value in reshape_object["shape"].get_list():
                            tmp_reshape = reshape_value.get_int()

                            if tmp_reshape is not None:
                                _reshape.append(tmp_reshape)

                _config.add_input(
                    _name, TensorDataType(_data_type), _dims, reshape=_reshape
                )

        def add_outputs(_config: ModelConfig, _value: Optional[PbtxtValue]):
            if _value is None:
                return

            for input_item in _value.get_list():
                input_item_object = input_item.get_object()

                if (
                    "name" not in input_item_object
                    or "data_type" not in input_item_object
                    or "dims" not in input_item_object
                ):
                    continue

                _name = input_item_object["name"].get_string()
                _data_type = input_item_object["data_type"].get_identifier()
                _dims: List[int] = []
                _reshape: List[int] = []

                if _name is None or _data_type is None:
                    continue

                for dim_value in input_item_object["dims"].get_list():
                    tmp_dim = dim_value.get_int()

                    if tmp_dim is not None:
                        _dims.append(tmp_dim)

                if "reshape" in input_item_object:
                    reshape_object = input_item_object["reshape"].get_object()

                    if "shape" in reshape_object:
                        for reshape_value in reshape_object["shape"].get_list():
                            tmp_reshape = reshape_value.get_int()

                            if tmp_reshape is not None:
                                _reshape.append(tmp_reshape)

                _config.add_output(
                    _name, TensorDataType(_data_type), _dims, reshape=_reshape
                )

        config: Optional["ModelConfig"] = None

        try:
            with open(path, "r") as file:
                parser = PbtxtParser(file.read())
                result = parser.parse()

                if result is None:
                    client_logger.info("Failed to parse model config from pbtxt.")
                    return config

                name_value = result.get_value("name")
                platform_value = result.get_value("platform")
                max_batch_size_value = result.get_value("max_batch_size")

                if name_value is None or platform_value is None:
                    client_logger.info("Failed to get name and platform from pbtxt.")
                    return config

                _name = name_value.get_string()
                _platform = platform_value.get_string()
                _max_batch_size: int = 0

                if _name is None or _platform is None:
                    client_logger.info("Failed to get name and platform from pbtxt.")
                    return config

                if max_batch_size_value is None:
                    _max_batch_size = 0
                else:
                    tmp_max_batch_size = max_batch_size_value.get_int()

                    if tmp_max_batch_size is None:
                        _max_batch_size = 0
                    else:
                        _max_batch_size = tmp_max_batch_size

                config = ModelConfig(
                    _name, platform=_platform, max_batch_size=_max_batch_size
                )

                add_inputs(config, result.get_value("input"))
                add_outputs(config, result.get_value("output"))
        except Exception as e:
            client_logger.error(
                f"Failed to parse model config from pbtxt.\n[Exception] {e}"
            )

        return config
