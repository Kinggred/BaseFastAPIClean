from pydantic import BaseSettings, Field, PostgresDsn, validator


class Database(BaseSettings):
    POSTGRES_HOST: str = Field(env="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(env="POSTGRES_PORT")
    POSTGRES_DB: str = Field(env="POSTGRES_DB")
    POSTGRES_USER: str = Field(env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(env="POSTGRES_PASSWORD")
    POSTGRES_DSN: str = Field(env="POSTGRES_DSN")

    @validator("POSTGRES_DSN")
    def set_postgres_dsn(cls, current_value, values):
        if current_value:
            return current_value
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_HOST"),
            port=values.get("POSTGRES_PORT"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )
