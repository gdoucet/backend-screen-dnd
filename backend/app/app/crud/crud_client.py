from typing import List

# from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.client import Client
from app.schemas.client import ClientCreate, ClientUpdate


class CRUDClient(CRUDBase[Client, ClientCreate, ClientUpdate]):
    def get_by_register_id(self, db: Session, *, register_id: str) -> Client:
        return (
            db.query(self.model)
            .filter(register_id == register_id)
            .first()
        )



client = CRUDClient(Client)