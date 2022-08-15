from typing import Any
from fastapi import APIRouter
from app.core.mqtt import mqtt

router = APIRouter()


data = [
    {
        "name": "toto"
    },
    {
        "name": "tata"
    }
]


@router.get("/")
def read_images() -> Any:
    return data


@router.get("/{id}")
def read_image(id: int) -> Any:
    mqtt.publish("/mqtt", "Hello from Fastapi")
    return data[id]
