import sys
from abc import abstractmethod
from enum import Enum
from typing import Any, ClassVar, Optional, Self, Union

from pydantic_core import core_schema

from bit.bitarray import BitArray
from bit.endian import Endian, convert_machine_endian


UNDEFINED = object()


class BaseDNSType:
    LENGTH: ClassVar[int] = UNDEFINED  # Length in bits
    ENDIAN: ClassVar[Endian] = Endian.LITTLE  # Network endianness
    EXTRA: Union[type, list[type]]

    def __init__(self, value: Any):
        """Initializes the object."""

        # Transform and validate the value
        value = self.transform(value)
        self.validate(value, self._get_core_schema())

        self.value = value

    @classmethod
    def transform(cls, value: Any) -> Any:
        if isinstance(value, cls):
            return value.value
        return value

    @classmethod
    @convert_machine_endian
    def _read_bits(cls, data: BitArray, length: Optional[int] = None) -> list[int]:
        return data.read(length or cls.LENGTH)

    @classmethod
    @convert_machine_endian
    def _peek_bits(cls, data: BitArray, length: int = None, offset: int = 0) -> list[int]:
        return data.peek(length or cls.LENGTH, offset)

    @classmethod
    @convert_machine_endian
    def _read_bytes(cls, data: BitArray, length: int) -> bytearray:
        return data.read_bytes(length)

    @classmethod
    def peek(cls, data: BitArray) -> Self:
        """Peek at next bits. Keep position unchanged."""

        return cls.from_bits(BitArray.from_bits(cls._peek_bits(data)))

    @classmethod
    @abstractmethod
    def from_bits(cls, data: BitArray, ctx: Optional[dict[str, Any]] = None) -> Self:
        """Parses a value from a bitarray."""

    @convert_machine_endian
    def to_bits(self) -> list[int]:
        """Converts the object to a bitarray."""

        return self._to_bits()

    @abstractmethod
    def _to_bits(self) -> list[int]:
        """Inner method to convert value to bits."""

    @classmethod
    @abstractmethod
    def _validate(cls, value: Any, info: core_schema.ValidationInfo) -> Any:
        """Validates a value."""

    @classmethod
    def validate(cls, value: Any, info: core_schema.ValidationInfo) -> Any:
        """Validates a value."""

        if isinstance(value, cls):
            return value

        return cls._validate(value, info)

    @classmethod
    @abstractmethod
    def _get_core_schema(cls):
        pass

    @classmethod
    def __get_pydantic_core_schema__(cls, source, handler):
        return core_schema.with_info_plain_validator_function(
            cls.validate,
            metadata=cls._get_core_schema(),
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value})"

    def __hash__(self) -> int:
        return hash(self.value)

    def __bool__(self):
        return bool(self.value)

    def __eq__(self, other: Any | Self) -> bool:
        if isinstance(other, self.__class__):
            return self.value == other.value
        return self.value == other

    def __ne__(self, other: Any | Self) -> bool:
        if isinstance(other, self.__class__):
            return self.value != other.value
        return self.value != other

    def __lt__(self, other: Any | Self) -> bool:
        if isinstance(other, self.__class__):
            return self.value < other.value
        return self.value < other

    def __le__(self, other: Any | Self) -> bool:
        if isinstance(other, self.__class__):
            return self.value <= other.value
        return self.value <= other

    def __gt__(self, other: Any | Self) -> bool:
        if isinstance(other, self.__class__):
            return self.value > other.value
        return self.value > other

    def __ge__(self, other: Any | Self) -> bool:
        if isinstance(other, self.__class__):
            return self.value >= other.value
        return self.value >= other

    def __add__(self, other: Any | Self) -> Self:
        if isinstance(other, self.__class__):
            return self.__class__(self.value + other.value)
        return self.__class__(self.value + other)

    def __sub__(self, other: Any | Self) -> Self:
        if isinstance(other, self.__class__):
            return self.__class__(self.value - other.value)
        return self.__class__(self.value - other)

    def __mul__(self, other: Any | Self) -> Self:
        if isinstance(other, self.__class__):
            return self.__class__(self.value * other.value)
        return self.__class__(self.value * other)

    def __truediv__(self, other: Any | Self) -> Self:
        if isinstance(other, self.__class__):
            return self.__class__(self.value / other.value)
        return self.__class__(self.value / other)

    def __floordiv__(self, other: Any | Self) -> Self:
        if isinstance(other, self.__class__):
            return self.__class__(self.value // other.value)
        return self.__class__(self.value // other)

    def __mod__(self, other: Any | Self) -> Self:
        if isinstance(other, self.__class__):
            return self.__class__(self.value % other.value)
        return self.__class__(self.value % other)

    def __pow__(self, other: Any | Self) -> Self:
        if isinstance(other, self.__class__):
            return self.__class__(self.value ** other.value)
        return self.__class__(self.value ** other)
