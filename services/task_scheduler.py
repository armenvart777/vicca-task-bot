from __future__ import annotations

import asyncio
import logging

import asyncpg
from aiogram import Bot

from db.queries.task_applications import (
    get_expired_applications,
    update_application_status,
)

logger = logging.getLogger(__name__)


async def check_expired_applications(pool: asyncpg.Pool, bot: Bot):
    ...
