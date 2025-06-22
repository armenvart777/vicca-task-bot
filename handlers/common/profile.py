from __future__ import annotations

from aiogram import F, Router
from aiogram.types import CallbackQuery

import asyncpg

from db.queries.blogger_profiles import get_blogger_platforms
from keyboards.callbacks import BloggerDashCB, ProfileCB
from keyboards.inline import blogger_dashboard_keyboard, customer_dashboard_keyboard
from utils.formatting import format_platform, format_price, format_rating

router = Router(name="common_profile")


@router.callback_query(BloggerDashCB.filter(F.action == "reviews"))
async def show_reviews(
    callback: CallbackQuery,
    pool: asyncpg.Pool,
    blogger_profile: asyncpg.Record | None,
):
    ...
