from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud.crud_client import client
from app.db.db import get_db

router = APIRouter()

@router.get("/")
def read_images(db = Depends(get_db)) -> Any:
    return client.get_multi(db)

@router.get("/{id}")
def read_image(id: int, db = Depends(get_db)) -> Any:
    return client.get(db, id=id)

@router.delete("/{id}")
def delete_client(id: int, db = Depends(get_db)) -> Any:
    return client.remove(db, id=id)
