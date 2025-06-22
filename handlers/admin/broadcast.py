from __future__ import annotations

import logging

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, Message

import asyncpg
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.queries.users import get_all_user_ids, get_user_ids_by_role
from filters.admin_filter import IsAdmin
from keyboards.callbacks import AdminConfirmCB, AdminPanelCB, BroadcastAudienceCB
from keyboards.inline import admin_panel_keyboard, confirm_keyboard
from states.admin_states import AdminBroadcastStates

logger = logging.getLogger(__name__)

router = Router(name="admin_broadcast")
router.message.filter(IsAdmin())
router.callback_query.filter(IsAdmin())

AUDIENCE_LABELS = {
    "all": "всем",
    "bloggers": "блогерам",
    "customers": "заказчикам",
}


def broadcast_audience_keyboard():
    ...

@router.callback_query(AdminPanelCB.filter(F.section == "broadcast"))
async def start_broadcast(callback: CallbackQuery, state: FSMContext):
    ...

@router.callback_query(
    AdminBroadcastStates.waiting_audience,
    BroadcastAudienceCB.filter(),
)
async def choose_audience(
    callback: CallbackQuery,
    callback_data: BroadcastAudienceCB,
    state: FSMContext,
):
    ...

@router.message(AdminBroadcastStates.waiting_message)
async def process_broadcast_text(message: Message, state: FSMContext):
    ...

@router.callback_query(
    AdminBroadcastStates.confirming,
    AdminConfirmCB.filter((F.action == "yes") & (F.target == "broadcast")),
)
async def confirm_broadcast(
    callback: CallbackQuery,
    state: FSMContext,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(
    AdminBroadcastStates.confirming,
    AdminConfirmCB.filter((F.action == "no") & (F.target == "broadcast")),
)
async def cancel_broadcast(callback: CallbackQuery, state: FSMContext):
    ...
