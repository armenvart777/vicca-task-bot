from __future__ import annotations

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, Message

import asyncpg
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.queries.statistics import get_detailed_stats, get_platform_stats
from filters.admin_filter import IsAdmin
from keyboards.callbacks import AdminPanelCB
from keyboards.inline import admin_panel_keyboard
from utils.formatting import format_price

router = Router(name="admin_panel")
router.message.filter(IsAdmin())
router.callback_query.filter(IsAdmin())


@router.message(Command("admin"))
async def cmd_admin(message: Message, state: FSMContext):
    ...

@router.callback_query(AdminPanelCB.filter(F.section == "main"))
async def admin_main(callback: CallbackQuery, state: FSMContext):
    ...

@router.callback_query(AdminPanelCB.filter(F.section == "stats"))
async def admin_stats_menu(callback: CallbackQuery):
    ...

def _back_to_stats_kb() -> InlineKeyboardBuilder:
    ...

@router.callback_query(AdminPanelCB.filter(F.section == "stats_overview"))
async def stats_overview(callback: CallbackQuery, pool: asyncpg.Pool):
    ...

@router.callback_query(AdminPanelCB.filter(F.section == "stats_users"))
async def stats_users(callback: CallbackQuery, pool: asyncpg.Pool):
    ...

@router.callback_query(AdminPanelCB.filter(F.section == "stats_tasks"))
async def stats_tasks(callback: CallbackQuery, pool: asyncpg.Pool):
    ...

@router.callback_query(AdminPanelCB.filter(F.section == "stats_finance"))
async def stats_finance(callback: CallbackQuery, pool: asyncpg.Pool):
    ...

@router.callback_query(AdminPanelCB.filter(F.section == "recent_tx"))
async def recent_transactions(callback: CallbackQuery, pool: asyncpg.Pool):
    ...

@router.callback_query(AdminPanelCB.filter(F.section == "stats_tops"))
async def stats_tops(callback: CallbackQuery, pool: asyncpg.Pool):
    ...
