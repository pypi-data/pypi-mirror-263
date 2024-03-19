from enum import Enum
from functools import lru_cache
from typing import cast

from ..extensions import Enums


class ListUsersSort(Enums.KnownString):
    NAME = "name"
    CREATEDAT = "createdAt"
    MODIFIEDAT = "modifiedAt"
    NAMEASC = "name:asc"
    NAMEDESC = "name:desc"
    MODIFIEDATASC = "modifiedAt:asc"
    MODIFIEDATDESC = "modifiedAt:desc"
    CREATEDATASC = "createdAt:asc"
    CREATEDATDESC = "createdAt:desc"

    def __str__(self) -> str:
        return str(self.value)

    @staticmethod
    @lru_cache(maxsize=None)
    def of_unknown(val: str) -> "ListUsersSort":
        if not isinstance(val, str):
            raise ValueError(f"Value of ListUsersSort must be a string (encountered: {val})")
        newcls = Enum("ListUsersSort", {"_UNKNOWN": val}, type=Enums.UnknownString)  # type: ignore
        return cast(ListUsersSort, getattr(newcls, "_UNKNOWN"))
