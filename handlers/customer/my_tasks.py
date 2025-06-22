from __future__ import annotations

from aiogram import F, Router
from aiogram.types import CallbackQuery, InlineKeyboardButton

import asyncpg
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.queries.tasks import (
    activate_task,
    get_customer_tasks,
    get_task,
    update_task_status,
)
from db.queries.customer_profiles import update_customer_balance
from db.queries.transactions import create_transaction
from keyboards.callbacks import CustomerDashCB, CustomerTaskCB, TaskPaymentCB
from keyboards.inline import (
    customer_dashboard_keyboard,
    customer_task_keyboard,
)
from utils.formatting import (
    format_payment_type,
    format_platforms_list,
    format_price,
    format_status,
)

router = Router(name="customer_my_tasks")


@router.callback_query(CustomerDashCB.filter(F.action == "my_tasks"))
async def show_my_tasks(
    callback: CallbackQuery,
    pool: asyncpg.Pool,
    customer_profile: asyncpg.Record | None,
):
    ...

@router.callback_query(CustomerTaskCB.filter(F.action == "view"))
async def view_task(
    callback: CallbackQuery,
    callback_data: CustomerTaskCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(TaskPaymentCB.filter(F.action == "pay"))
async def pay_for_task(
    callback: CallbackQuery,
    callback_data: TaskPaymentCB,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
    customer_profile: asyncpg.Record | None,
):
    ...

@router.callback_query(CustomerTaskCB.filter(F.action == "pause"))
async def pause_task(
    callback: CallbackQuery,
    callback_data: CustomerTaskCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(CustomerTaskCB.filter(F.action == "resume"))
async def resume_task(
    callback: CallbackQuery,
    callback_data: CustomerTaskCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(CustomerTaskCB.filter(F.action == "cancel"))
async def cancel_task(
    callback: CallbackQuery,
    callback_data: CustomerTaskCB,
    pool: asyncpg.Pool,
):
    ...
