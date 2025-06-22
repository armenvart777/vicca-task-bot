from __future__ import annotations

from aiogram.fsm.state import State, StatesGroup


class CustomerRegistration(StatesGroup):
    waiting_name = State()
    waiting_city = State()
    waiting_phone = State()
    waiting_country = State()
    waiting_business_area = State()
    waiting_services = State()
    confirming = State()


class CreateTask(StatesGroup):
    waiting_name = State()
    waiting_task_type = State()
    waiting_subcategory = State()
    waiting_site_link = State()
    waiting_description = State()
    waiting_video_limit = State()
    waiting_blogger_size = State()
    waiting_country = State()
    waiting_platforms = State()
    waiting_payment_type = State()
    waiting_pricing_options = State()
    waiting_fix_price = State()
    waiting_bonus_views_amount = State()
    waiting_views_threshold = State()
    waiting_bonus_repeats_amount = State()
    waiting_repeats_threshold = State()
    waiting_product_price = State()
    waiting_barter_description = State()
    waiting_hashtags = State()
    waiting_deadline = State()
    confirming = State()
