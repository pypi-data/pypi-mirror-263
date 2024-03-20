"""
Lightweight and simple ORM for Python (with psycopg)
"""
__version__ = "1.0.0"
from .config import DNS
from .base import DataBase
from .types import (
    BigInt,
    BigSerial,
    Boolean,
    Date,
    Float,
    Integer,
    JSON,
    Password,
    Real,
    Serial,
    SmallInt,
    SmallSerial,
    Text,
    Time,
    TimeStamp,
    UUID,
    VarChar,
    XML,
    Model,
)

__all__ = [
    "DNS",
    "DataBase",
    "Model",
    "BigInt",
    "BigSerial",
    "Boolean",
    "Date",
    "Float",
    "Integer",
    "JSON",
    "Password",
    "Real",
    "Serial",
    "SmallInt",
    "SmallSerial",
    "Text",
    "Time",
    "TimeStamp",
    "UUID",
    "VarChar",
    "XML",
]
