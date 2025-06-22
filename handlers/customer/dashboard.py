from __future__ import annotations

from aiogram import F, Router
from aiogram.types import CallbackQuery, Message

import asyncpg

from db.queries.customer_profiles import get_customer_by_user
from db.queries.tasks import get_customer_tasks
from keyboards.callbacks import CustomerDashCB
from keyboards.inline import customer_dashboard_keyboard
from utils.formatting import format_price

router = Router(name="customer_dashboard")


async def _dashboard_text(pool: asyncpg.Pool, customer_profile) -> str:
    ...

async def show_customer_dashboard(
    message: Message, pool: asyncpg.Pool, user_db: asyncpg.Record
):
    ...

async def show_customer_dashboard_cb(
    callback: CallbackQuery,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
    customer_profile: asyncpg.Record,
):
    ...

@router.callback_query(CustomerDashCB.filter(F.action == "back"))
async def customer_dash_back(
    callback: CallbackQuery,
    pool: asyncpg.Pool,
    customer_profile: asyncpg.Record | None,
):
    ...
