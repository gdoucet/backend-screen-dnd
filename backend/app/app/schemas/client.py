from http import client
from typing import Optional

from pydantic import BaseModel


# Shared properties
class ClientBase(BaseModel):
    register_id: Optional[str] = None


# Properties to receive on Client creation
class ClientCreate(ClientBase):
    register_id: str


# Properties to receive on Client update
class ClientUpdate(ClientBase):
    pass


# Properties shared by models stored in DB
class ClientInDBBase(ClientBase):
    id: int
    register_id: str

    class Config:
        orm_mode = True


# Properties to return to client
class Client(ClientInDBBase):
    pass


# Properties properties stored in DB
class ClientInDB(ClientInDBBase):
    pass