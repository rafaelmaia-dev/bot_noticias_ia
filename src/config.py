from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file_encoding="UTF-8", env_file=".env")
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_CHAT_ID: int
    GROQ_API_KEY: str
    DATABASE_URL: str
    

settings = Settings()

