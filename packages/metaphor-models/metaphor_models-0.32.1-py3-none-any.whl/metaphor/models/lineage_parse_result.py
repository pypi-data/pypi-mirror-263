from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, Callable, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Target(Enum):
    CLL = "CLL"
    OTHERS = "OTHERS"
    TLL = "TLL"


@dataclass
class ParseWarning:
    message: Optional[str] = None
    target: Optional[Target] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ParseWarning':
        assert isinstance(obj, dict)
        message = from_union([from_str, from_none], obj.get("message"))
        target = from_union([Target, from_none], obj.get("target"))
        return ParseWarning(message, target)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.message is not None:
            result["message"] = from_union([from_str, from_none], self.message)
        if self.target is not None:
            result["target"] = from_union([lambda x: to_enum(Target, x), from_none], self.target)
        return result


@dataclass
class LineageParseResult:
    sql: Optional[str] = None
    warnings: Optional[List[ParseWarning]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LineageParseResult':
        assert isinstance(obj, dict)
        sql = from_union([from_str, from_none], obj.get("sql"))
        warnings = from_union([lambda x: from_list(ParseWarning.from_dict, x), from_none], obj.get("warnings"))
        return LineageParseResult(sql, warnings)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.sql is not None:
            result["sql"] = from_union([from_str, from_none], self.sql)
        if self.warnings is not None:
            result["warnings"] = from_union([lambda x: from_list(lambda x: to_class(ParseWarning, x), x), from_none], self.warnings)
        return result


def lineage_parse_result_from_dict(s: Any) -> LineageParseResult:
    return LineageParseResult.from_dict(s)


def lineage_parse_result_to_dict(x: LineageParseResult) -> Any:
    return to_class(LineageParseResult, x)
