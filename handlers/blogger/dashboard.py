from __future__ import annotations

from aiogram import F, Router
from aiogram.types import CallbackQuery, Message

import asyncpg

from db.queries.blogger_profiles import get_blogger_by_user, get_blogger_platforms
from keyboards.callbacks import BloggerDashCB
from keyboards.inline import blogger_dashboard_keyboard
from utils.formatting import format_platform, format_price, format_rating

router = Router(name="blogger_dashboard")


async def _dashboard_text(pool: asyncpg.Pool, user_db, blogger_profile) -> str:
    ...

async def show_blogger_dashboard(
    message: Message, pool: asyncpg.Pool, user_db: asyncpg.Record
):
    ...

async def show_blogger_dashboard_cb(
    callback: CallbackQuery,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
    blogger_profile: asyncpg.Record,
):
    ...

@router.callback_query(BloggerDashCB.filter(F.action == "back"))
async def blogger_dash_back(
    callback: CallbackQuery,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
    blogger_profile: asyncpg.Record | None,
):
    ...
