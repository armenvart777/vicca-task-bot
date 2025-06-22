from __future__ import annotations

from aiogram import F, Router
from aiogram.types import CallbackQuery, InlineKeyboardButton

import asyncpg
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.queries.tasks import get_task, get_tasks_by_status, update_task_status
from db.queries.task_applications import get_task_applications
from filters.admin_filter import IsAdmin
from keyboards.callbacks import AdminPanelCB, AdminTaskCB, AdminBloggerCB
from keyboards.inline import admin_panel_keyboard
from utils.formatting import (
    format_blogger_size,
    format_payment_type,
    format_platforms_list,
    format_price,
    format_status,
)

router = Router(name="admin_tasks")
router.callback_query.filter(IsAdmin())

STATUS_LABELS = {
    "active": "🟢 Активные",
    "pending_moderation": "🟡 На модерации",
    "pending_payment": "🟠 Ожидают оплаты",
    "paused": "⏸ Приостановленные",
    "completed": "✅ Завершённые",
    "cancelled": "🚫 Отменённые",
}

APP_STATUS_EMOJI = {
    "pending": "⏳",
    "in_progress": "🔄",
    "approved": "✅",
    "rejected": "❌",
    "cancelled": "🚫",
}


@router.callback_query(AdminPanelCB.filter(F.section == "tasks"))
async def show_tasks(callback: CallbackQuery, pool: asyncpg.Pool):
    ...

@router.callback_query(AdminTaskCB.filter(F.action.startswith("list_")))
async def show_tasks_list(
    callback: CallbackQuery,
    callback_data: AdminTaskCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(AdminTaskCB.filter(F.action == "view"))
async def view_task_admin(
    callback: CallbackQuery,
    callback_data: AdminTaskCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(AdminTaskCB.filter(F.action == "apps"))
async def task_applications_list(
    callback: CallbackQuery,
    callback_data: AdminTaskCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(AdminTaskCB.filter(F.action == "pause"))
async def pause_task_admin(
    callback: CallbackQuery,
    callback_data: AdminTaskCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(AdminTaskCB.filter(F.action == "activate"))
async def activate_task_admin(
    callback: CallbackQuery,
    callback_data: AdminTaskCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(AdminTaskCB.filter(F.action == "cancel_confirm"))
async def cancel_task_confirm(
    callback: CallbackQuery,
    callback_data: AdminTaskCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(AdminTaskCB.filter(F.action == "cancel_do"))
async def cancel_task_do(
    callback: CallbackQuery,
    callback_data: AdminTaskCB,
    pool: asyncpg.Pool,
):
    ...
