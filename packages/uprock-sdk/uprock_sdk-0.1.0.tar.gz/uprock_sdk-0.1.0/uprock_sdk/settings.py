from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_URL: str = "http://localhost"

    NAMESPACE_ID: Optional[int] = None

    def update(self, data: dict) -> "Settings":
        update = self.dict()
        update.update(data)

        for k, v in self.validate(update).dict(exclude_defaults=True).items():
            setattr(self, k, v)
        return self


GLOBAL_SETTINGS = Settings()
