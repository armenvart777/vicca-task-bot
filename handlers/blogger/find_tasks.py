from __future__ import annotations

from aiogram import F, Router
from aiogram.types import CallbackQuery, InlineKeyboardButton

import asyncpg
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.queries.blogger_profiles import get_blogger_platforms, get_max_subscribers
from db.queries.blogger_profiles import get_blogger_size
from db.queries.categories import get_all_categories
from db.queries.task_applications import get_application_by_task_blogger
from db.queries.tasks import get_active_tasks_for_blogger, get_task, increment_videos_taken
from db.queries.task_applications import create_application
from keyboards.callbacks import BloggerDashCB, TaskBrowseCB, TaskCategoryCB
from keyboards.inline import (
    blogger_dashboard_keyboard,
    task_categories_keyboard,
    task_detail_blogger_keyboard,
)
from utils.formatting import (
    format_blogger_size,
    format_payment_type,
    format_platforms_list,
    format_price,
)

router = Router(name="blogger_find_tasks")


@router.callback_query(BloggerDashCB.filter(F.action == "find_tasks"))
async def find_tasks_categories(
    callback: CallbackQuery,
    pool: asyncpg.Pool,
    blogger_profile: asyncpg.Record | None,
):
    ...

@router.callback_query(TaskCategoryCB.filter())
async def filter_tasks(
    callback: CallbackQuery,
    callback_data: TaskCategoryCB,
    pool: asyncpg.Pool,
    blogger_profile: asyncpg.Record | None,
):
    ...

@router.callback_query(TaskBrowseCB.filter(F.action == "view"))
async def view_task(
    callback: CallbackQuery,
    callback_data: TaskBrowseCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(TaskBrowseCB.filter(F.action == "take"))
async def take_task(
    callback: CallbackQuery,
    callback_data: TaskBrowseCB,
    pool: asyncpg.Pool,
    blogger_profile: asyncpg.Record | None,
):
    ...
