from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr
