from __future__ import annotations

from aiogram.filters import Filter
from aiogram.types import CallbackQuery, Message, TelegramObject

from config import settings


class IsAdmin(Filter):
    async def __call__(self, event: TelegramObject, **kwargs) -> bool:
        ...
