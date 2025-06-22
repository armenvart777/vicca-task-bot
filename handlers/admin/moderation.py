from __future__ import annotations

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import asyncpg

from db.queries.tasks import get_task, get_tasks_by_status, update_task_status
from filters.admin_filter import IsAdmin
from keyboards.callbacks import AdminModerateCB, AdminPanelCB
from keyboards.inline import admin_moderate_task_keyboard, admin_panel_keyboard
from services.notifications import notify_user
from states.admin_states import AdminModerationStates
from utils.formatting import (
    format_blogger_size,
    format_payment_type,
    format_platforms_list,
    format_price,
)

router = Router(name="admin_moderation")
router.message.filter(IsAdmin())
router.callback_query.filter(IsAdmin())


@router.callback_query(AdminPanelCB.filter(F.section == "moderation"))
async def show_moderation_list(callback: CallbackQuery, pool: asyncpg.Pool):
    ...

@router.callback_query(AdminModerateCB.filter(F.action == "view"))
async def view_task_moderation(
    callback: CallbackQuery,
    callback_data: AdminModerateCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(AdminModerateCB.filter(F.action == "approve"))
async def approve_task(
    callback: CallbackQuery,
    callback_data: AdminModerateCB,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
):
    ...

@router.callback_query(AdminModerateCB.filter(F.action == "reject"))
async def reject_task_start(
    callback: CallbackQuery,
    callback_data: AdminModerateCB,
    state: FSMContext,
):
    ...

@router.message(AdminModerationStates.waiting_reject_reason)
async def reject_task_reason(
    message: Message,
    state: FSMContext,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
):
    ...
