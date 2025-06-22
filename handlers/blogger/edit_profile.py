from __future__ import annotations

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import asyncpg

from db.queries.blogger_profiles import (
    add_blogger_platform,
    delete_blogger_platforms,
    get_blogger_platforms,
    update_blogger_profile,
)
from keyboards.callbacks import BarterCB, BloggerCountryCB, BloggerPlatformCB, ProfileCB, RegBackCB
from keyboards.inline import (
    barter_keyboard,
    blogger_country_keyboard,
    blogger_dashboard_keyboard,
    blogger_platform_keyboard,
    reg_back_keyboard,
)
from states.blogger_states import BloggerEditProfile
from utils.validators import validate_phone, validate_subscribers, validate_url

router = Router(name="blogger_edit_profile")

TARGET = "edit_blogger"


@router.callback_query(ProfileCB.filter(F.action == "edit_blogger"))
async def start_edit_profile(
    callback: CallbackQuery,
    state: FSMContext,
    pool: asyncpg.Pool,
    blogger_profile: asyncpg.Record | None,
):
    ...

# === Кнопки Назад ===

@router.callback_query(
    BloggerEditProfile.waiting_name,
    RegBackCB.filter(F.target == TARGET),
)
async def back_from_name(callback: CallbackQuery, state: FSMContext):
    ...

@router.callback_query(
    BloggerEditProfile.waiting_city,
    RegBackCB.filter(F.target == TARGET),
)
async def back_from_city(callback: CallbackQuery, state: FSMContext):
    ...

@router.callback_query(
    BloggerEditProfile.waiting_phone,
    RegBackCB.filter(F.target == TARGET),
)
async def back_from_phone(callback: CallbackQuery, state: FSMContext):
    ...

@router.callback_query(
    BloggerEditProfile.waiting_country,
    RegBackCB.filter(F.target == TARGET),
)
async def back_from_country(callback: CallbackQuery, state: FSMContext):
    ...

@router.callback_query(
    BloggerEditProfile.waiting_barter,
    RegBackCB.filter(F.target == TARGET),
)
async def back_from_barter(callback: CallbackQuery, state: FSMContext):
    ...

@router.callback_query(
    BloggerEditProfile.waiting_platforms,
    RegBackCB.filter(F.target == TARGET),
)
async def back_from_platforms(callback: CallbackQuery, state: FSMContext):
    ...

@router.callback_query(
    BloggerEditProfile.waiting_platform_link,
    RegBackCB.filter(F.target == TARGET),
)
async def back_from_link(callback: CallbackQuery, state: FSMContext):
    ...

@router.callback_query(
    BloggerEditProfile.waiting_platform_subscribers,
    RegBackCB.filter(F.target == TARGET),
)
async def back_from_subscribers(callback: CallbackQuery, state: FSMContext):
    ...

@router.callback_query(
    BloggerEditProfile.confirming,
    RegBackCB.filter(F.target == TARGET),
)
async def back_from_confirm(callback: CallbackQuery, state: FSMContext):
    ...

# === Обработка ввода ===

@router.message(BloggerEditProfile.waiting_name)
async def process_name(message: Message, state: FSMContext):
    ...

@router.message(BloggerEditProfile.waiting_city)
async def process_city(message: Message, state: FSMContext):
    ...

@router.message(BloggerEditProfile.waiting_phone)
async def process_phone(message: Message, state: FSMContext):
    ...

@router.callback_query(
    BloggerEditProfile.waiting_country, BloggerCountryCB.filter()
)
async def process_country_cb(
    callback: CallbackQuery,
    callback_data: BloggerCountryCB,
    state: FSMContext,
):
    ...

@router.message(BloggerEditProfile.waiting_country)
async def process_country_text(message: Message, state: FSMContext):
    ...

@router.callback_query(
    BloggerEditProfile.waiting_barter, BarterCB.filter()
)
async def process_barter_cb(
    callback: CallbackQuery,
    callback_data: BarterCB,
    state: FSMContext,
):
    ...

@router.message(BloggerEditProfile.waiting_barter)
async def process_barter_text(message: Message, state: FSMContext):
    ...

async def _show_platforms(callback: CallbackQuery, state: FSMContext):
    ...

async def _show_platforms_msg(message: Message, state: FSMContext):
    ...

@router.message(BloggerEditProfile.waiting_platforms)
async def skip_platforms(message: Message, state: FSMContext):
    ...

@router.callback_query(
    BloggerEditProfile.waiting_platforms,
    BloggerPlatformCB.filter(F.action == "select"),
)
async def toggle_platform(
    callback: CallbackQuery,
    callback_data: BloggerPlatformCB,
    state: FSMContext,
):
    ...

@router.callback_query(
    BloggerEditProfile.waiting_platforms,
    BloggerPlatformCB.filter(F.action == "done"),
)
async def platforms_done(callback: CallbackQuery, state: FSMContext):
    ...

@router.message(BloggerEditProfile.waiting_platform_link)
async def process_platform_link(message: Message, state: FSMContext):
    ...

@router.message(BloggerEditProfile.waiting_platform_subscribers)
async def process_subscribers(message: Message, state: FSMContext):
    ...

async def _show_confirm(target: Message, state: FSMContext):
    ...

@router.message(BloggerEditProfile.confirming)
async def confirm_edit(
    message: Message,
    state: FSMContext,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
):
    ...
