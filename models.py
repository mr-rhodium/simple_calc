from pydantic import BaseModel


class CalcQuery(BaseModel):
    left: int
    sign: str
    right: int
