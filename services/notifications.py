from __future__ import annotations

import logging

import asyncpg
from aiogram import Bot

from config import settings

logger = logging.getLogger(__name__)


async def notify_admins(bot: Bot, pool: asyncpg.Pool, text: str) -> None:
    ...

async def notify_user(
    bot: Bot, user_id: int, text: str, reply_markup=None,
) -> None:
    ...

async def notify_matching_bloggers(
    bot: Bot, pool: asyncpg.Pool, task_id: int
) -> int:
    """Notify bloggers who match a newly activated task. Returns count sent."""
    ...
