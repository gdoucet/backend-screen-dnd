from pydantic import BaseSettings
from fastapi_mqtt import MQTTConfig


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    MQTT_HOST: str = "mqtt"
    MQTT_PORT: int = 1883
    MQTT_KEEPALIVE: int = 60


settings = Settings()

mqtt_config = MQTTConfig(
    host=settings.MQTT_HOST,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)
