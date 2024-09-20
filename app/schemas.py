from pydantic import BaseModel


class WriteDataRequest(BaseModel):
    phone: str
    address: str
