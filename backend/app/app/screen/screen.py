from app.crud.crud_client import client
from app.db.session import SessionLocal
from app.schemas.client import ClientCreate

def register_client(register_id: str) -> None:
    db = SessionLocal()
    screen_client = client.get_by_register_id(db=db, register_id=register_id)
    if not screen_client:
        client.create(db=db, obj_in=ClientCreate(register_id=register_id))
