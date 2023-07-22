from typing import Any
from dataclasses import dataclass


@dataclass
class User:
    nickname: str
    name: str
    picture: str
    updated_at: str
    email: str
    sub: str
    token: str

    @staticmethod
    def from_dict(obj: Any) -> "User":
        _nickname = str(obj.get("nickname"))
        _name = str(obj.get("name"))
        _picture = str(obj.get("picture"))
        _updated_at = str(obj.get("updated_at"))
        _email = str(obj.get("email"))
        _sub = str(obj.get("sub"))
        _token = str(obj.get("token"))
        return User(_nickname, _name, _picture, _updated_at, _email, _sub, _token)
