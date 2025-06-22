from __future__ import annotations

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import asyncpg

from db.queries.customer_profiles import create_customer_profile
from db.queries.users import set_user_role
from keyboards.callbacks import CustomerCountryCB, RegBackCB
from keyboards.inline import customer_country_keyboard, customer_dashboard_keyboard, reg_back_keyboard
from states.customer_states import CustomerRegistration
from utils.validators import validate_phone

router = Router(name="customer_registration")

TARGET = "customer"


async def start_customer_registration(callback: CallbackQuery, state: FSMContext):
    ...

# === Кнопки Назад ===

@router.callback_query(
    CustomerRegistration.waiting_name,
    RegBackCB.filter(F.target == TARGET),
)
async def back_from_name(callback: CallbackQuery, state: FSMContext):
    ...

@router.callback_query(
    CustomerRegistration.waiting_city,
    RegBackCB.filter(F.target == TARGET),
)
async def back_from_city(callback: CallbackQuery, state: FSMContext):
    ...

@router.callback_query(
    CustomerRegistration.waiting_phone,
    RegBackCB.filter(F.target == TARGET),
)
async def back_from_phone(callback: CallbackQuery, state: FSMContext):
    ...

@router.callback_query(
    CustomerRegistration.waiting_country,
    RegBackCB.filter(F.target == TARGET),
)
async def back_from_country(callback: CallbackQuery, state: FSMContext):
    ...

@router.callback_query(
    CustomerRegistration.waiting_business_area,
    RegBackCB.filter(F.target == TARGET),
)
async def back_from_business(callback: CallbackQuery, state: FSMContext):
    ...

@router.callback_query(
    CustomerRegistration.waiting_services,
    RegBackCB.filter(F.target == TARGET),
)
async def back_from_services(callback: CallbackQuery, state: FSMContext):
    ...

@router.callback_query(
    CustomerRegistration.confirming,
    RegBackCB.filter(F.target == TARGET),
)
async def back_from_confirm(callback: CallbackQuery, state: FSMContext):
    ...

# === Обработка ввода ===

@router.message(CustomerRegistration.waiting_name)
async def process_name(message: Message, state: FSMContext):
    ...

@router.message(CustomerRegistration.waiting_city)
async def process_city(message: Message, state: FSMContext):
    ...

@router.message(CustomerRegistration.waiting_phone)
async def process_phone(message: Message, state: FSMContext):
    ...

@router.callback_query(
    CustomerRegistration.waiting_country, CustomerCountryCB.filter()
)
async def process_country(
    callback: CallbackQuery,
    callback_data: CustomerCountryCB,
    state: FSMContext,
):
    ...

@router.message(CustomerRegistration.waiting_business_area)
async def process_business(message: Message, state: FSMContext):
    ...

@router.message(CustomerRegistration.waiting_services)
async def process_services(message: Message, state: FSMContext):
    ...

@router.message(CustomerRegistration.confirming)
async def confirm_registration(
    message: Message,
    state: FSMContext,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
):
    ...
