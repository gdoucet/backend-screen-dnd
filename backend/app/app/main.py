from fastapi.responses import RedirectResponse
from app.api.api_v1.api import api_router
from app.core.config import settings
from app.core.app_fastapi import app
from app.core.mqtt import mqtt
from app.screen.screen import register_client
from app.db.base_class import Base
from app.db.session import engine


Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix=settings.API_V1_STR)

@mqtt.on_connect()
def connect(client, flags, rc, properties):
    mqtt.client.subscribe("screen/#")  # subscribing mqtt topic
    print("Connected: ", client, flags, rc, properties)


@mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    if topic == "screen/register":
        register_client("clientid")
    print("Received message: ", topic, payload.decode(), qos, properties)


@mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("Disconnected")


@mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    print("subscribed", client, mid, qos, properties)


@app.get("/", response_class=RedirectResponse)
async def redirect_to_api() -> RedirectResponse:
    return RedirectResponse("/api/")
