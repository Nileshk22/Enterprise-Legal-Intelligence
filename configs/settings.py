from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str

    LOG_LEVEL: str = "INFO"

    TOP_K: int = 5

    EMBEDDING_MODEL: str
    RERANKER_MODEL: str

    LLM_PROVIDER: str

    class Config:
        env_file = ".env"


settings = Settings()