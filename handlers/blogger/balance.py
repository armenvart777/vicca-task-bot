from __future__ import annotations

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, Message

import asyncpg
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.queries.blogger_profiles import update_blogger_balance
from db.queries.payment_requests import (
    create_payment_request,
    get_setting,
    get_user_pending_request,
)
from db.queries.transactions import create_transaction, get_user_transactions
from keyboards.callbacks import BalanceCB, BloggerDashCB
from keyboards.inline import balance_keyboard, blogger_dashboard_keyboard
from services.notifications import notify_admins
from states.common_states import WithdrawalStates
from utils.formatting import format_price

router = Router(name="blogger_balance")


@router.callback_query(BloggerDashCB.filter(F.action == "balance"))
async def show_balance(
    callback: CallbackQuery,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
    blogger_profile: asyncpg.Record | None,
):
    ...

@router.callback_query(BalanceCB.filter((F.action == "withdraw") & (F.role == "blogger")))
async def start_withdrawal(
    callback: CallbackQuery,
    state: FSMContext,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
    blogger_profile: asyncpg.Record | None,
):
    ...

@router.message(WithdrawalStates.waiting_amount)
async def process_withdrawal_amount(
    message: Message,
    state: FSMContext,
    pool: asyncpg.Pool,
    blogger_profile: asyncpg.Record | None,
):
    ...

@router.message(WithdrawalStates.waiting_sbp_details)
async def process_sbp_details(
    message: Message,
    state: FSMContext,
):
    ...

@router.callback_query(
    WithdrawalStates.confirming,
    BalanceCB.filter((F.action == "confirm_withdraw") & (F.role == "blogger")),
)
async def confirm_withdrawal(
    callback: CallbackQuery,
    state: FSMContext,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
    blogger_profile: asyncpg.Record | None,
):
    ...

@router.callback_query(
    WithdrawalStates.confirming,
    BalanceCB.filter((F.action == "cancel_withdraw") & (F.role == "blogger")),
)
async def cancel_withdrawal(callback: CallbackQuery, state: FSMContext):
    ...

@router.callback_query(BalanceCB.filter((F.action == "history") & (F.role == "blogger")))
async def show_history(
    callback: CallbackQuery,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
):
    ...
