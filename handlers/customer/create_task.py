from __future__ import annotations

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import asyncpg

from db.queries.tasks import create_task, get_next_order_number
from keyboards.callbacks import (
    BloggerSizeCB,
    CountryCB,
    CustomerDashCB,
    PaymentTypeCB,
    PlatformSelectCB,
    PricingOptionCB,
    TaskSubcategoryCB,
    TaskTypeCB,
)
from keyboards.inline import (
    blogger_size_keyboard,
    country_keyboard,
    customer_dashboard_keyboard,
    payment_type_keyboard,
    platforms_select_keyboard,
    pricing_options_keyboard,
    task_subcategory_keyboard,
    task_type_keyboard,
)
from services.notifications import notify_admins
from states.customer_states import CreateTask
from utils.formatting import (
    format_blogger_size,
    format_payment_type,
    format_platforms_list,
    format_price,
)

router = Router(name="customer_create_task")

# Минимальные суммы по размеру блогера
MIN_PRICING = {
    "small":  {"fix": 1000, "bonus": 500},
    "medium": {"fix": 2500, "bonus": 1000},
    "large":  {"fix": 5000, "bonus": 2000},
}

BACK_HINT = "\n\n(или «назад» чтобы вернуться на шаг назад)"


def _is_back(text: str | None) -> bool:
    ...

@router.callback_query(CustomerDashCB.filter(F.action == "create_task"))
async def start_create_task(
    callback: CallbackQuery,
    state: FSMContext,
    customer_profile: asyncpg.Record | None,
):
    ...

@router.message(CreateTask.waiting_name)
async def process_name(message: Message, state: FSMContext):
    ...

@router.callback_query(CreateTask.waiting_task_type, TaskTypeCB.filter())
async def process_task_type(
    callback: CallbackQuery,
    callback_data: TaskTypeCB,
    state: FSMContext,
):
    ...

@router.callback_query(CreateTask.waiting_subcategory, TaskSubcategoryCB.filter())
async def process_subcategory(
    callback: CallbackQuery,
    callback_data: TaskSubcategoryCB,
    state: FSMContext,
):
    ...

@router.message(CreateTask.waiting_site_link)
async def process_site_link(message: Message, state: FSMContext):
    ...

@router.message(CreateTask.waiting_description)
async def process_description(message: Message, state: FSMContext):
    ...

@router.message(CreateTask.waiting_video_limit)
async def process_video_limit(message: Message, state: FSMContext):
    ...

@router.callback_query(CreateTask.waiting_blogger_size, BloggerSizeCB.filter())
async def process_blogger_size(
    callback: CallbackQuery,
    callback_data: BloggerSizeCB,
    state: FSMContext,
):
    ...

@router.callback_query(CreateTask.waiting_country, CountryCB.filter())
async def process_country(
    callback: CallbackQuery,
    callback_data: CountryCB,
    state: FSMContext,
):
    ...

@router.callback_query(
    CreateTask.waiting_platforms,
    PlatformSelectCB.filter(F.action == "toggle"),
)
async def toggle_platform(
    callback: CallbackQuery,
    callback_data: PlatformSelectCB,
    state: FSMContext,
):
    ...

@router.callback_query(
    CreateTask.waiting_platforms,
    PlatformSelectCB.filter(F.action == "done"),
)
async def platforms_done(callback: CallbackQuery, state: FSMContext):
    ...

@router.callback_query(CreateTask.waiting_payment_type, PaymentTypeCB.filter())
async def process_payment_type(
    callback: CallbackQuery,
    callback_data: PaymentTypeCB,
    state: FSMContext,
):
    ...

# === Платный тип: выбор опций оплаты кнопками ===


@router.callback_query(
    CreateTask.waiting_pricing_options,
    PricingOptionCB.filter(F.action == "noop"),
)
async def pricing_fix_noop(callback: CallbackQuery):
    """Фикс обязателен — нельзя отключить."""
    ...

@router.callback_query(
    CreateTask.waiting_pricing_options,
    PricingOptionCB.filter(F.action == "toggle"),
)
async def toggle_pricing_option(
    callback: CallbackQuery,
    callback_data: PricingOptionCB,
    state: FSMContext,
):
    ...

@router.callback_query(
    CreateTask.waiting_pricing_options,
    PricingOptionCB.filter(F.action == "done"),
)
async def pricing_options_done(callback: CallbackQuery, state: FSMContext):
    ...

async def _ask_next_pricing_amount(message, state, selected, edit=False):
    """Спрашивает сумму для следующей выбранной опции."""
    ...

def _get_prev_pricing_state(data: dict, current: str):
    """Возвращает предыдущий state для кнопки назад в pricing."""
    ...

@router.message(CreateTask.waiting_fix_price)
async def process_fix_price(message: Message, state: FSMContext):
    ...

@router.message(CreateTask.waiting_bonus_views_amount)
async def process_bonus_views_amount(message: Message, state: FSMContext):
    ...

@router.message(CreateTask.waiting_views_threshold)
async def process_views_threshold(message: Message, state: FSMContext):
    ...

@router.message(CreateTask.waiting_bonus_repeats_amount)
async def process_bonus_repeats_amount(message: Message, state: FSMContext):
    ...

@router.message(CreateTask.waiting_repeats_threshold)
async def process_repeats_threshold(message: Message, state: FSMContext):
    ...

@router.message(CreateTask.waiting_product_price)
async def process_product_price(message: Message, state: FSMContext):
    ...

@router.message(CreateTask.waiting_barter_description)
async def process_barter_description(message: Message, state: FSMContext):
    ...

@router.message(CreateTask.waiting_hashtags)
async def process_hashtags(message: Message, state: FSMContext):
    ...

@router.message(CreateTask.waiting_deadline)
async def process_deadline(message: Message, state: FSMContext):
    ...

@router.message(CreateTask.confirming)
async def confirm_task(
    message: Message,
    state: FSMContext,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
    customer_profile: asyncpg.Record,
):
    ...
