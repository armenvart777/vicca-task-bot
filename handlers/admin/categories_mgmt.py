from __future__ import annotations

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, Message

import asyncpg
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.queries.categories import (
    create_category,
    delete_category,
    get_all_categories,
    toggle_category,
)
from filters.admin_filter import IsAdmin
from keyboards.callbacks import AdminCategoryCB, AdminPanelCB
from keyboards.inline import admin_panel_keyboard
from states.admin_states import AdminCategoryStates

router = Router(name="admin_categories")
router.message.filter(IsAdmin())
router.callback_query.filter(IsAdmin())


@router.callback_query(AdminPanelCB.filter(F.section == "categories"))
async def show_categories(callback: CallbackQuery, pool: asyncpg.Pool):
    ...

@router.callback_query(AdminCategoryCB.filter(F.action == "toggle"))
async def toggle_cat(
    callback: CallbackQuery,
    callback_data: AdminCategoryCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(AdminCategoryCB.filter(F.action == "add"))
async def add_category_start(callback: CallbackQuery, state: FSMContext):
    ...

@router.message(AdminCategoryStates.waiting_name)
async def add_category_name(message: Message, state: FSMContext):
    ...

@router.message(AdminCategoryStates.waiting_emoji)
async def add_category_emoji(
    message: Message, state: FSMContext, pool: asyncpg.Pool
):
    ...
