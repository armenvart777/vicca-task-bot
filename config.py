from __future__ import annotations

import os
from dataclasses import dataclass, field

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "postgresql://vicca:vicca@localhost:5432/vicca_bot"
    )
    ADMIN_IDS: list[int] = field(default_factory=list)
    OFFER_URL: str = os.getenv("OFFER_URL", "")
    PRIVACY_URL: str = os.getenv("PRIVACY_URL", "")

    def __post_init__(self):
        ...

settings = Settings()
