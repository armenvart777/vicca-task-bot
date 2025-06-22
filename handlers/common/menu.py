from __future__ import annotations

import logging

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, Message

import asyncpg
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.queries.users import set_user_role
from keyboards.callbacks import MainMenuCB, ProfileCB
from keyboards.inline import (
    blogger_dashboard_keyboard,
    customer_dashboard_keyboard,
    role_select_keyboard,
)
from services.notifications import notify_admins
from states.common_states import SupportStates

logger = logging.getLogger(__name__)

router = Router(name="common_menu")


async def _safe_delete(msg: Message) -> None:
    ...

@router.callback_query(ProfileCB.filter(F.action == "switch_role"))
async def switch_role(
    callback: CallbackQuery,
    state: FSMContext,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
    active_role: str,
    blogger_profile,
    customer_profile,
):
    ...

def faq_keyboard(active_role: str):
    ...

@router.callback_query(MainMenuCB.filter(F.action == "guide"))
async def show_guide(callback: CallbackQuery, active_role: str):
    ...

@router.callback_query(MainMenuCB.filter(F.action == "faq"))
async def show_faq(callback: CallbackQuery, active_role: str):
    ...

@router.callback_query(MainMenuCB.filter(F.action == "support"))
async def start_support(callback: CallbackQuery, state: FSMContext):
    ...

@router.message(SupportStates.waiting_message)
async def process_support_message(
    message: Message,
    state: FSMContext,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
    active_role: str,
):
    ...
