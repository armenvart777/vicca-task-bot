from __future__ import annotations

from aiogram import F, Router
from aiogram.types import CallbackQuery, InlineKeyboardButton

import asyncpg
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.queries.task_applications import (
    get_application,
    get_blogger_applications,
    update_application_status,
)
from keyboards.callbacks import BloggerDashCB, MyTaskCB
from keyboards.inline import blogger_dashboard_keyboard, my_task_blogger_keyboard
from utils.formatting import format_payment_type, format_price, format_status

router = Router(name="blogger_my_tasks")


@router.callback_query(BloggerDashCB.filter(F.action == "my_tasks"))
async def show_my_tasks(
    callback: CallbackQuery,
    pool: asyncpg.Pool,
    blogger_profile: asyncpg.Record | None,
):
    ...

@router.callback_query(MyTaskCB.filter(F.action == "view"))
async def view_my_task(
    callback: CallbackQuery,
    callback_data: MyTaskCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(MyTaskCB.filter(F.action == "cancel"))
async def cancel_my_task(
    callback: CallbackQuery,
    callback_data: MyTaskCB,
    pool: asyncpg.Pool,
):
    ...
