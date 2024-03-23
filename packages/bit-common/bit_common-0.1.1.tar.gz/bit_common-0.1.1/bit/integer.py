from typing import ClassVar, Self, Union, cast

from bit.base import BaseType
from bit.bitarray import BitArray
from bit.endian import Endian

from pydantic.json_schema import GetJsonSchemaHandler, JsonSchemaValue
from pydantic_core import core_schema


class Integer(BaseType):
    ENDIAN: ClassVar[Endian] = Endian.BIG
    SIGNED: bool = True
    EXTRA = int

    @classmethod
    def _get_core_schema(cls):
        return core_schema.int_schema(
            ge=cls.min_value(),
            le=cls.max_value(),
            strict=True,
            ref=cls.__name__,
        )

    @classmethod
    def max_value(cls) -> int:
        return 2 ** (cls.LENGTH - 1) - 1 if cls.SIGNED else 2**cls.LENGTH - 1

    @classmethod
    def min_value(cls) -> int:
        return -(2 ** (cls.LENGTH - 1)) if cls.SIGNED else 0

    @classmethod
    def from_bits(cls, bits: BitArray, *args, **kwargs) -> Self:
        """Converts list of bits to integer."""

        return cls(sum([2**i * v for i, v in enumerate(cls._read_bits(bits))]))

    def _to_bits(self) -> list[int]:
        """Converts integer to list of bits."""

        if not self.SIGNED:
            return [(self.value >> i) & 1 for i in range(self.LENGTH)]
        else:
            return [(self.value >> i) & 1 for i in range(self.LENGTH - 1)] + [int(self.value < 0)]

    @classmethod
    def transform(cls, value: Union[bool, int, list[int]]) -> int:
        """Converts value to integer."""

        if isinstance(value, bool):
            return int(value)

        if isinstance(value, list):
            if len(value) != cls.LENGTH:
                raise ValueError(f"Expected {cls.LENGTH} bits, got {len(value)}.")

            if any(bit not in (0, 1) for bit in value):
                raise ValueError("Expected 0 or 1.")

            return sum([2**i * v for i, v in enumerate(reversed(value))])

        return super().transform(value)

    @classmethod
    def _validate(
        cls,
        value: Union[int, Self],
        info: core_schema.ValidationInfo,
    ) -> int:
        """Validates a value."""

        if isinstance(value, bool):
            return int(value)

        if isinstance(value, list):
            if len(value) != cls.LENGTH:
                raise ValueError(f"Expected {cls.LENGTH} bits, got {len(value)}.")

            if any(bit not in (0, 1) for bit in value):
                raise ValueError("Expected 0 or 1.")

            return sum([2**i * v for i, v in enumerate(reversed(value))])

        elif isinstance(value, int):
            if not cls.min_value() <= value <= cls.max_value():
                raise ValueError(
                    f"Expected {cls.min_value()} <= value <= {cls.max_value()}, got {value}."
                )
            return value

        elif isinstance(value, Integer):
            return value.value

        else:
            raise ValueError(f"Expected int or list of bits, got {type(value)}.")

    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: core_schema.JsonSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        """Returns JSON schema for integer."""

        return {
            "type": "integer",
            "minimum": cls.min_value(),
            "maximum": cls.max_value(),
        }

    def __repr__(self):
        return f"{self.value}"


class UnsignedInteger(Integer):
    SIGNED = False


class Boolean(UnsignedInteger):
    LENGTH = 1
    EXTRA = bool

    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: core_schema.JsonSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        return {"type": "boolean"}

    @classmethod
    def _validate(
        cls,
        value: Union[int, list[int], bool],
        info: core_schema.ValidationInfo,
    ) -> int:
        if isinstance(value, bool):
            return value

        return super()._validate(value, info)


def _generate_int_type(int_length: int, int_type: type[Integer]) -> type[Integer]:
    return cast(type[int_type], type(f"int{int_length}", (int_type,), {"LENGTH": int_length}))


# Generate integer types
int1 = _generate_int_type(1, Integer)
int2 = _generate_int_type(2, Integer)
int3 = _generate_int_type(3, Integer)
int4 = _generate_int_type(4, Integer)
int8 = _generate_int_type(8, Integer)
int16 = _generate_int_type(16, Integer)
int32 = _generate_int_type(32, Integer)
int64 = _generate_int_type(64, Integer)
int128 = _generate_int_type(128, Integer)


# Generate unsigned integer types
uint1 = _generate_int_type(1, UnsignedInteger)
uint2 = _generate_int_type(2, UnsignedInteger)
uint3 = _generate_int_type(3, UnsignedInteger)
uint4 = _generate_int_type(4, UnsignedInteger)
uint8 = _generate_int_type(8, UnsignedInteger)
uint16 = _generate_int_type(16, UnsignedInteger)
uint32 = _generate_int_type(32, UnsignedInteger)
uint64 = _generate_int_type(64, UnsignedInteger)
uint128 = _generate_int_type(128, UnsignedInteger)


# Generate special types
boolean = _generate_int_type(1, Boolean)
