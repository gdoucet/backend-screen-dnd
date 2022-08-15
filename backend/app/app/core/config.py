from pydantic import (
    BaseSettings,
    validator,
    PostgresDsn
)
from fastapi_mqtt import MQTTConfig
from typing import Optional, Dict, Any


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    MQTT_HOST: str = "mqtt"
    MQTT_PORT: int = 1883
    MQTT_KEEPALIVE: int = 60
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )


settings = Settings()

mqtt_config = MQTTConfig(
    host=settings.MQTT_HOST,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)
