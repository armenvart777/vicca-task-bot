from __future__ import annotations

from aiogram import F, Router
from aiogram.types import CallbackQuery, InlineKeyboardButton

import asyncpg
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.queries.payment_requests import (
    get_pending_requests,
    get_payment_request,
    update_request_status,
)
from db.queries.customer_profiles import get_customer_by_user, update_customer_balance
from db.queries.blogger_profiles import get_blogger_by_user, update_blogger_balance
from db.queries.transactions import create_transaction
from filters.admin_filter import IsAdmin
from keyboards.callbacks import AdminPanelCB, AdminPayRequestCB
from services.notifications import notify_user
from utils.formatting import format_price

router = Router(name="admin_payments")
router.callback_query.filter(IsAdmin())


@router.callback_query(AdminPanelCB.filter(F.section == "payments"))
async def payments_menu(callback: CallbackQuery, pool: asyncpg.Pool):
    ...

@router.callback_query(AdminPanelCB.filter(F.section == "pay_deposits"))
async def list_deposits(callback: CallbackQuery, pool: asyncpg.Pool):
    ...

@router.callback_query(AdminPanelCB.filter(F.section == "pay_withdrawals"))
async def list_withdrawals(callback: CallbackQuery, pool: asyncpg.Pool):
    ...

@router.callback_query(AdminPayRequestCB.filter(F.action == "view"))
async def view_request(
    callback: CallbackQuery,
    callback_data: AdminPayRequestCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(AdminPayRequestCB.filter(F.action == "approve"))
async def approve_request(
    callback: CallbackQuery,
    callback_data: AdminPayRequestCB,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
):
    ...

@router.callback_query(AdminPayRequestCB.filter(F.action == "reject"))
async def reject_request(
    callback: CallbackQuery,
    callback_data: AdminPayRequestCB,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
):
    ...
