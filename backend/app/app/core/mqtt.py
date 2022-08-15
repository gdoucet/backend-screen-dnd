from app.core.config import mqtt_config
from app.core.app_fastapi import app
from fastapi_mqtt import FastMQTT

mqtt = FastMQTT(
    config=mqtt_config
)

mqtt.init_app(app)
