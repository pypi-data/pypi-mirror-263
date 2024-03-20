from enum import Enum
from re import match as regex_match
from typing import Any, cast, Dict, List, Optional, Tuple


class PbtxtValueType(Enum):
    BOOL = "bool"
    FLOAT = "float"
    IDENTIFIER = "identifier"
    INT = "int"
    INVALID = "invalid"
    LIST = "list"
    OBJECT = "object"
    STRING = "string"


class PbtxtValue:
    __type: PbtxtValueType
    __data: Any

    def __init__(self, data: Any, data_type: PbtxtValueType):
        self.__data = data
        self.__type = data_type

    def get_type(self) -> PbtxtValueType:
        return self.__type

    def get_bool(self) -> Optional[bool]:
        if self.__type == PbtxtValueType.BOOL:
            return self.__data
        return None

    def get_float(self) -> Optional[float]:
        if self.__type == PbtxtValueType.FLOAT:
            return self.__data
        return None

    def get_identifier(self) -> Optional[str]:
        if self.__type == PbtxtValueType.IDENTIFIER:
            return self.__data
        return None

    def get_int(self) -> Optional[int]:
        if self.__type == PbtxtValueType.INT:
            return self.__data
        return None

    def get_string(self) -> Optional[str]:
        if self.__type == PbtxtValueType.STRING:
            return self.__data
        return None

    def get_list(self) -> List["PbtxtValue"]:
        if self.__type != PbtxtValueType.LIST:
            return []

        result: List["PbtxtValue"] = []

        try:
            for item in self.__data:
                result.append(item)
        except Exception:
            return []

        return result

    def get_object(self) -> Dict[str, "PbtxtValue"]:
        if self.__type != PbtxtValueType.OBJECT:
            return {}

        result: Dict[str, "PbtxtValue"] = {}

        try:
            for item in self.__data:
                item = cast("PbtxtField", item)
                result[item.key] = item.value
        except Exception:
            return {}

        return result


class PbtxtField:
    __key: str
    __value: PbtxtValue

    def __init__(self, key: str, value: PbtxtValue):
        self.__key = key
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @property
    def value(self) -> PbtxtValue:
        return self.__value


class PbtxtObject:
    __data: List[PbtxtField]

    def __init__(self, data: List[PbtxtField]):
        self.__data = data

    def __getitem__(self, key: str) -> Optional[PbtxtValue]:
        for field in self.__data:
            if field.key == key:
                return field.value

        return None

    def __iter__(self):
        for field in self.__data:
            yield field

        return None


class PbtxtList:
    __data: List[PbtxtValue]
    __index: int

    def __init__(self, data: List[PbtxtValue]):
        self.__data = data
        self.__index = 0

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self) -> PbtxtValue:
        if self.__index >= len(self.__data):
            raise StopIteration

        result = self.__data[self.__index]
        self.__index += 1

        return result

    def __getitem__(self, index: int) -> Optional[PbtxtValue]:
        if index < 0 or index >= len(self.__data):
            return None

        return self.__data[index]


class PbtxtDocument:
    __data: List[PbtxtField]

    def __init__(self, data: List[PbtxtField]):
        self.__data = data

    def get_value(self, key: str) -> Optional[PbtxtValue]:
        for field in self.__data:
            if field.key == key:
                return field.value

        return None


class PbtxtParser:
    __lines: List[str]

    def __init__(self, content: str):
        self.__lines = content.split("\n")

    def __parse_string(
        self,
        line_number: int,
        col_number: int,
    ) -> Tuple[PbtxtValue, int, int]:
        string_value: str = ""
        cur_line_number: int = line_number
        cur_col_number: int = col_number
        cur_line = self.__lines[line_number].strip()

        while cur_col_number < len(cur_line):
            if cur_line[cur_col_number] == '"':
                return (
                    PbtxtValue(string_value, PbtxtValueType.STRING),
                    (
                        cur_line_number
                        if cur_col_number + 1 < len(cur_line)
                        else (cur_line_number + 1)
                    ),
                    (cur_col_number + 1) if cur_col_number + 1 < len(cur_line) else 0,
                )

            string_value += cur_line[cur_col_number]
            cur_col_number += 1

        return (PbtxtValue(None, PbtxtValueType.INVALID), 0, 0)

    def __parse_number(
        self,
        line_number: int,
        col_number: int,
    ) -> Tuple[PbtxtValue, int, int]:
        number_value: str = ""
        cur_line_number: int = line_number
        cur_col_number: int = col_number
        cur_line = self.__lines[line_number].strip()

        while cur_col_number < len(cur_line):
            if (
                cur_line[cur_col_number] == ","
                or cur_line[cur_col_number] == "]"
                or cur_line[cur_col_number] == "}"
            ):
                cur_col_number += 1 if cur_line[cur_col_number] == "," else 0
                break
            elif cur_line[cur_col_number] == "#":
                cur_line_number += 1
                cur_col_number = 0
                break
            else:
                number_value += cur_line[cur_col_number]
                cur_col_number += 1

        number_value = number_value.strip()

        if regex_match(r"-?\s*\d+", number_value):
            return (
                PbtxtValue(int(number_value), PbtxtValueType.INT),
                (
                    cur_line_number
                    if cur_col_number < len(cur_line)
                    else (cur_line_number + 1)
                ),
                cur_col_number if cur_col_number < len(cur_line) else 0,
            )
        elif regex_match(
            r"-?\s*(\d+(\.\d+)?|\.\d+)([eE][\-\+]?\d+)?[fF]?", number_value
        ):
            return (
                PbtxtValue(float(number_value.rstrip("fF")), PbtxtValueType.FLOAT),
                (
                    cur_line_number
                    if cur_col_number < len(cur_line)
                    else (cur_line_number + 1)
                ),
                cur_col_number if cur_col_number < len(cur_line) else 0,
            )

        return (PbtxtValue(None, PbtxtValueType.INVALID), 0, 0)

    def __parse_identifier(
        self,
        line_number: int,
        col_number: int,
    ) -> Tuple[PbtxtValue, int, int]:
        identifier_value: str = ""
        cur_line_number: int = line_number
        cur_col_number: int = col_number
        cur_line = self.__lines[line_number].strip()

        if not regex_match(r"[a-zA-Z_]", cur_line[col_number]):
            return (PbtxtValue(None, PbtxtValueType.INVALID), 0, 0)
        else:
            identifier_value += cur_line[col_number]
            cur_col_number += 1

        while cur_col_number < len(cur_line):
            if regex_match(r"[a-zA-Z0-9_]", cur_line[cur_col_number]):
                identifier_value += cur_line[cur_col_number]
                cur_col_number += 1
            elif cur_line[cur_col_number] == "#":
                cur_line_number = cur_line_number + 1
                cur_col_number = 0
                break
            else:
                break

        return (
            PbtxtValue(identifier_value, PbtxtValueType.IDENTIFIER),
            (
                cur_line_number
                if cur_col_number < len(cur_line)
                else (cur_line_number + 1)
            ),
            cur_col_number if cur_col_number < len(cur_line) else 0,
        )

    def __parse_key(
        self,
        line_number: int,
        col_number: int,
    ) -> Tuple[str, int, int]:
        key: str = ""
        cur_line_number: int = line_number
        cur_col_number: int = col_number
        cur_line = self.__lines[line_number].strip()
        is_space_encountered: bool = False

        if not regex_match(r"[a-zA-Z_]", cur_line[cur_col_number]):
            return ("", 0, 0)
        else:
            key += cur_line[col_number]
            cur_col_number += 1

        while cur_col_number < len(cur_line):
            if (
                regex_match(r"[a-zA-Z0-9_]", cur_line[cur_col_number])
                and not is_space_encountered
            ):
                key += cur_line[cur_col_number]
                cur_col_number += 1
            elif cur_line[cur_col_number] == " ":
                is_space_encountered = True
                cur_col_number += 1
            elif (
                cur_line[cur_col_number] == ":"
                or cur_line[cur_col_number] == "["
                or cur_line[cur_col_number] == "{"
            ):
                cur_col_number += 1 if cur_line[cur_col_number] == ":" else 0
                break
            elif cur_line[cur_col_number] == "#":
                cur_line_number += 1
                cur_col_number = 0
            else:
                return ("", 0, 0)

        return (
            key,
            (
                cur_line_number
                if cur_col_number < len(cur_line)
                else (cur_line_number + 1)
            ),
            cur_col_number if cur_col_number < len(cur_line) else 0,
        )

    def __parse_value(
        self,
        line_number: int,
        col_number: int,
    ) -> Tuple[PbtxtValue, int, int]:
        """
        Returns:
            Tuple[PbtxtValue, int, int]: the first element is the value; the second element is the next line number; the third element is the next column number
        """

        cur_line_number = line_number
        cur_col_number = col_number
        is_line_number_set: bool = False

        while cur_line_number < len(self.__lines):
            cur_line = self.__lines[cur_line_number].strip()

            while cur_col_number < len(cur_line):
                if cur_line[cur_col_number] == "[":  # list
                    list_cur_line_number: int = (
                        cur_line_number
                        if cur_col_number + 1 < len(cur_line)
                        else (cur_line_number + 1)
                    )
                    list_cur_col_number: int = (
                        (cur_col_number + 1)
                        if cur_col_number + 1 < len(cur_line)
                        else 0
                    )
                    list_cur_line: str = self.__lines[list_cur_line_number].strip()
                    value_list: List[PbtxtValue] = []

                    while list_cur_line[list_cur_col_number] != "]":
                        (
                            value,
                            list_next_line_number,
                            list_next_col_number,
                        ) = self.__parse_value(
                            list_cur_line_number, list_cur_col_number
                        )

                        if value.get_type() == PbtxtValueType.INVALID:
                            return (PbtxtValue(None, PbtxtValueType.INVALID), 0, 0)
                        else:
                            value_list.append(value)
                            list_cur_line_number = list_next_line_number
                            list_cur_col_number = list_next_col_number
                            list_cur_line = self.__lines[list_cur_line_number].strip()

                    return (
                        PbtxtValue(value_list, PbtxtValueType.LIST),
                        (
                            list_cur_line_number
                            if list_cur_col_number + 1 < len(list_cur_line)
                            else (list_cur_line_number + 1)
                        ),
                        (
                            (list_cur_col_number + 1)
                            if list_cur_col_number + 1 < len(list_cur_line)
                            else 0
                        ),
                    )
                elif cur_line[cur_col_number] == "{":  # object
                    object_cur_line_number: int = (
                        cur_line_number
                        if cur_col_number + 1 < len(cur_line)
                        else (cur_line_number + 1)
                    )
                    object_cur_col_number: int = (
                        (cur_col_number + 1)
                        if cur_col_number + 1 < len(cur_line)
                        else 0
                    )
                    object_cur_line: str = self.__lines[object_cur_line_number].strip()
                    field_list: List[PbtxtField] = []

                    while object_cur_line[object_cur_col_number] != "}":
                        if object_cur_line[object_cur_col_number] == " ":
                            object_cur_col_number += 1

                            if object_cur_col_number >= len(object_cur_line):
                                object_cur_line_number += 1
                                object_cur_col_number = 0
                                object_cur_line = self.__lines[
                                    object_cur_line_number
                                ].strip()

                            continue
                        elif object_cur_line[object_cur_col_number] == "#":
                            object_cur_line_number += 1
                            object_cur_col_number = 0
                            object_cur_line = self.__lines[
                                object_cur_line_number
                            ].strip()
                            continue

                        (
                            object_key,
                            object_value_next_line_number,
                            object_value_next_col_number,
                        ) = self.__parse_key(
                            object_cur_line_number, object_cur_col_number
                        )

                        if object_key == "":
                            return (PbtxtValue(None, PbtxtValueType.INVALID), 0, 0)

                        (
                            object_value,
                            object_next_line_number,
                            object_next_col_number,
                        ) = self.__parse_value(
                            object_value_next_line_number, object_value_next_col_number
                        )

                        if object_value.get_type() == PbtxtValueType.INVALID:
                            return (PbtxtValue(None, PbtxtValueType.INVALID), 0, 0)

                        field_list.append(PbtxtField(object_key, object_value))
                        object_cur_line_number = object_next_line_number
                        object_cur_col_number = object_next_col_number
                        object_cur_line = self.__lines[object_cur_line_number].strip()

                    return (
                        PbtxtValue(field_list, PbtxtValueType.OBJECT),
                        (
                            object_cur_line_number
                            if object_cur_col_number + 1 < len(object_cur_line)
                            else (object_cur_line_number + 1)
                        ),
                        (
                            (object_cur_col_number + 1)
                            if object_cur_col_number + 1 < len(object_cur_line)
                            else 0
                        ),
                    )
                elif cur_line[cur_col_number] == '"':  # string
                    return self.__parse_string(
                        (
                            cur_line_number
                            if cur_col_number + 1 < len(cur_line)
                            else (cur_line_number + 1)
                        ),
                        (
                            (cur_col_number + 1)
                            if cur_col_number + 1 < len(cur_line)
                            else 0
                        ),
                    )
                elif regex_match(
                    r"[0-9\-\.]", cur_line[cur_col_number]
                ):  # int or float
                    return self.__parse_number(cur_line_number, cur_col_number)
                elif regex_match(r"\w", cur_line[cur_col_number]):  # identifier
                    return self.__parse_identifier(cur_line_number, cur_col_number)
                elif (
                    cur_line[cur_col_number] == " " or cur_line[cur_col_number] == ","
                ):  #  space or comma
                    cur_col_number += 1
                elif cur_line[cur_col_number] == "#":  #  comment
                    cur_line_number += 1
                    cur_col_number = 0
                    is_line_number_set = True
                    break
                else:  # invalid
                    return (PbtxtValue(None, PbtxtValueType.INVALID), 0, 0)

            if not is_line_number_set:
                cur_line_number += 1
                cur_col_number = 0

        return (PbtxtValue(None, PbtxtValueType.INVALID), 0, 0)

    def parse(self) -> Optional[PbtxtDocument]:
        field_list: List[PbtxtField] = []
        cur_line_number: int = 0
        cur_col_number: int = 0

        while cur_line_number < len(self.__lines):
            if (
                self.__lines[cur_line_number].strip() == ""
                or self.__lines[cur_line_number].strip()[0] == "#"
            ):
                cur_line_number += 1
                cur_col_number = 0
                continue

            (cur_key, value_next_line_number, value_next_col_number) = self.__parse_key(
                cur_line_number, cur_col_number
            )

            if cur_key == "":
                return None

            (
                cur_value,
                next_line_number,
                next_col_number,
            ) = self.__parse_value(value_next_line_number, value_next_col_number)

            if cur_value.get_type() == PbtxtValueType.INVALID:
                return None

            field_list.append(PbtxtField(cur_key, cur_value))
            cur_line_number = next_line_number
            cur_col_number = next_col_number

        return PbtxtDocument(field_list)
