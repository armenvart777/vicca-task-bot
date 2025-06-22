from __future__ import annotations

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, Message

import asyncpg
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.queries.payment_requests import (
    create_payment_request,
    get_setting,
    get_user_pending_request,
)
from db.queries.transactions import get_user_transactions
from keyboards.callbacks import BalanceCB, CustomerDashCB, PayMethodCB
from keyboards.inline import balance_keyboard, customer_dashboard_keyboard
from services.notifications import notify_admins
from states.common_states import TopupStates
from utils.formatting import format_price

router = Router(name="customer_balance")


@router.callback_query(CustomerDashCB.filter(F.action == "balance"))
async def show_balance(
    callback: CallbackQuery,
    customer_profile: asyncpg.Record | None,
):
    ...

@router.callback_query(BalanceCB.filter((F.action == "topup") & (F.role == "customer")))
async def start_topup(
    callback: CallbackQuery,
    state: FSMContext,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
):
    ...

@router.message(TopupStates.waiting_amount)
async def process_topup_amount(
    message: Message,
    state: FSMContext,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(TopupStates.waiting_method, PayMethodCB.filter())
async def select_payment_method(
    callback: CallbackQuery,
    callback_data: PayMethodCB,
    state: FSMContext,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(
    TopupStates.waiting_confirmation,
    BalanceCB.filter((F.action == "confirm_topup") & (F.role == "customer")),
)
async def confirm_topup(
    callback: CallbackQuery,
    state: FSMContext,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
):
    ...

@router.callback_query(
    TopupStates.waiting_confirmation,
    BalanceCB.filter((F.action == "cancel_topup") & (F.role == "customer")),
)
async def cancel_topup(callback: CallbackQuery, state: FSMContext):
    ...

@router.callback_query(BalanceCB.filter((F.action == "history") & (F.role == "customer")))
async def show_history(
    callback: CallbackQuery,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
):
    ...
