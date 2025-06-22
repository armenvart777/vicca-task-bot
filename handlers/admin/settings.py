from __future__ import annotations

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, Message

import asyncpg
from aiogram.utils.keyboard import InlineKeyboardBuilder

from filters.admin_filter import IsAdmin
from keyboards.callbacks import AdminPanelCB, AdminSettingCB
from keyboards.inline import admin_panel_keyboard
from states.admin_states import AdminSettingsStates

router = Router(name="admin_settings")
router.message.filter(IsAdmin())
router.callback_query.filter(IsAdmin())


@router.callback_query(AdminPanelCB.filter(F.section == "settings"))
async def show_settings(callback: CallbackQuery, pool: asyncpg.Pool):
    ...

@router.callback_query(AdminSettingCB.filter())
async def edit_setting(
    callback: CallbackQuery,
    callback_data: AdminSettingCB,
    state: FSMContext,
):
    ...

@router.message(AdminSettingsStates.waiting_value)
async def save_setting(
    message: Message, state: FSMContext, pool: asyncpg.Pool
):
    ...
