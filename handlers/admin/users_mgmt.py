from __future__ import annotations

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, Message

import asyncpg
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.queries.blogger_profiles import get_blogger_by_user, get_blogger_platforms
from db.queries.customer_profiles import get_customer_by_user
from db.queries.statistics import (
    get_all_bloggers,
    get_all_customers,
    get_blogger_full,
    get_customer_full,
)
from db.queries.users import ban_user, get_user, search_users
from filters.admin_filter import IsAdmin
from keyboards.callbacks import (
    AdminBloggerCB,
    AdminCustomerCB,
    AdminPanelCB,
    AdminUserCB,
)
from keyboards.inline import admin_panel_keyboard
from states.admin_states import AdminUserSearchStates
from utils.formatting import format_platform, format_price

router = Router(name="admin_users")
router.message.filter(IsAdmin())
router.callback_query.filter(IsAdmin())


# ==================== Поиск пользователей ====================

@router.callback_query(AdminPanelCB.filter(F.section == "users"))
async def users_menu(callback: CallbackQuery):
    ...

@router.callback_query(AdminPanelCB.filter(F.section == "user_search"))
async def start_user_search(callback: CallbackQuery, state: FSMContext):
    ...

@router.message(AdminUserSearchStates.waiting_query)
async def process_search(message: Message, state: FSMContext, pool: asyncpg.Pool):
    ...

@router.callback_query(AdminUserCB.filter(F.action == "view"))
async def view_user(
    callback: CallbackQuery,
    callback_data: AdminUserCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(AdminUserCB.filter(F.action == "ban"))
async def ban_user_handler(
    callback: CallbackQuery,
    callback_data: AdminUserCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(AdminUserCB.filter(F.action == "unban"))
async def unban_user_handler(
    callback: CallbackQuery,
    callback_data: AdminUserCB,
    pool: asyncpg.Pool,
):
    ...

# ==================== Список блогеров ====================

@router.callback_query(AdminPanelCB.filter(F.section == "bloggers_list"))
async def bloggers_list(callback: CallbackQuery, pool: asyncpg.Pool):
    ...

@router.callback_query(AdminBloggerCB.filter(F.action == "view"))
async def view_blogger(
    callback: CallbackQuery,
    callback_data: AdminBloggerCB,
    pool: asyncpg.Pool,
):
    ...

# ==================== Список заказчиков ====================

@router.callback_query(AdminPanelCB.filter(F.section == "customers_list"))
async def customers_list(callback: CallbackQuery, pool: asyncpg.Pool):
    ...

@router.callback_query(AdminCustomerCB.filter(F.action == "view"))
async def view_customer(
    callback: CallbackQuery,
    callback_data: AdminCustomerCB,
    pool: asyncpg.Pool,
):
    ...
