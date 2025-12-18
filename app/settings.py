import os
from functools import lru_cache


class Settings:
    def __init__(self) -> None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY environment variable is required")

        self.OPENAI_API_KEY = api_key


@lru_cache()
def get_settings() -> Settings:
    return Settings()
