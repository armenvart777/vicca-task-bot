from __future__ import annotations

from aiogram.filters import Filter
from aiogram.types import TelegramObject


class IsBlogger(Filter):
    async def __call__(self, event: TelegramObject, **kwargs) -> bool:
        ...

class IsCustomer(Filter):
    async def __call__(self, event: TelegramObject, **kwargs) -> bool:
        ...

class IsRegistered(Filter):
    async def __call__(self, event: TelegramObject, **kwargs) -> bool:
        ...
