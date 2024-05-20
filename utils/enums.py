from enum import Enum


class RoleType(str, Enum):
    user = "user"
    seller = "seller"
    admin = "admin"
