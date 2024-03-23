from typing import Any, ClassVar, Optional, Self, Union

from bit.base import BaseType, UNDEFINED

from pydantic.json_schema import GetJsonSchemaHandler, JsonSchemaValue
from pydantic_core import core_schema

from bit.bitarray import BitArray


class String(BaseType):
    ENCODING: str = "ascii"
    LENGTH: ClassVar[int] = UNDEFINED
    SEPARATOR: ClassVar[list[int]] = [0] * 8
    EXTRA = str

    @classmethod
    def _get_core_schema(cls):
        return core_schema.str_schema(
            min_length=0,
            strict=True,
        )

    def transform(self, value: Any) -> Any:
        value = super().transform(value)

        return str(value)

    def _to_bits(self) -> list[int]:
        """Converts string to list of bits."""

        return BitArray.bytes_to_bits(self.value.encode(self.ENCODING))

    @classmethod
    def from_bits(
        cls,
        data: Union[BitArray, list[int]],
        ctx: Optional[dict[str, Any]] = None
    ) -> Self:
        """Parses a string from a bitarray."""

        from bit import int8

        if isinstance(data, list):
            data = BitArray.from_bits(data)

        result = ""

        ctx = ctx or {}

        length = ctx.get("length", None)

        if length is None:
            length = int8.from_bits(data).value

        result += cls._read_bytes(data, length).decode(cls.ENCODING)

        return cls(result)

    @classmethod
    def _validate(cls, value: Union[str, bytes, Self], info: core_schema.ValidationInfo) -> str:
        if isinstance(value, cls):
            value = value.value

        elif isinstance(value, bytes):
            value = value.decode(cls.ENCODING)

        elif not isinstance(value, str):
            raise ValueError(f"Expected str, got {type(value)}.")

        return value

    @classmethod
    def __get_pydantic_core_schema__(cls, *args):
        return core_schema.with_info_plain_validator_function(cls.validate)

    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: core_schema.JsonSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:

        return {
            "type": "string",
            "format": cls.ENCODING,
        }

    def __repr__(self):
        return f"{self.value}"


class StringWithPrefix(String):
    """String with length prefix in front."""

    def _to_bits(self) -> list[int]:
        """Converts string to list of bits."""

        from bit.integer import uint8

        return uint8(len(self.value))._to_bits() + super()._to_bits()

    @classmethod
    def from_bits(
        cls,
        data: Union[BitArray, list[int]],
        ctx: Optional[dict[str, Any]] = None
    ) -> Self:
        """Parses a string from a bitarray."""

        from bit.integer import uint8

        if isinstance(data, list):
            data = BitArray.from_bits(data)

        length = uint8.from_bits(BitArray(data.read_bytes(1))).value
        return super().from_bits(data, ctx={"length": length})


class ASCIIString(String):
    ENCODING: str = "ascii"


class ASCIIStringWithPrefix(ASCIIString, StringWithPrefix):
    pass


class UTF8String(String):
    ENCODING: str = "utf-8"


class UTF8StringWithPrefix(UTF8String, StringWithPrefix):
    pass
