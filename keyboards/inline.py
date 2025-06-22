from __future__ import annotations

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboards.callbacks import (
    AdminCategoryCB,
    AdminConfirmCB,
    AdminModerateCB,
    AdminPanelCB,
    AdminTaskCB,
    AdminUserCB,
    BalanceCB,
    BarterCB,
    BloggerCountryCB,
    BloggerDashCB,
    CustomerCountryCB,
    BloggerPlatformCB,
    BloggerSizeCB,
    CountryCB,
    CustomerDashCB,
    CustomerTaskCB,
    MainMenuCB,
    MyTaskCB,
    OfferCB,
    PaymentTypeCB,
    PlatformSelectCB,
    PricingOptionCB,
    ProfileCB,
    RegBackCB,
    ReportCB,
    ReviewRatingCB,
    RoleSelectCB,
    TaskBrowseCB,
    TaskCategoryCB,
    TaskPaymentCB,
    TaskSubcategoryCB,
    TaskTypeCB,
    VerifyReportCB,
)
from utils.formatting import format_platform, format_price, format_status
from utils.pagination import add_pagination_row, paginate


# === Общие ===

def reg_back_keyboard(target: str) -> InlineKeyboardMarkup:
    """Клавиатура с одной кнопкой 'Назад' для шагов регистрации."""
    ...

def barter_keyboard(back_target: str | None = None) -> InlineKeyboardMarkup:
    """Клавиатура Да/Нет для бартера с кнопкой Назад."""
    ...

def offer_keyboard() -> InlineKeyboardMarkup:
    ...

def role_select_keyboard() -> InlineKeyboardMarkup:
    ...

# === Блогер ===

def blogger_dashboard_keyboard() -> InlineKeyboardMarkup:
    ...

def blogger_platform_keyboard(
    selected: list[str] | None = None,
    back_target: str | None = None,
) -> InlineKeyboardMarkup:
    ...

def task_categories_keyboard(
    categories: list, page: int = 0
) -> InlineKeyboardMarkup:
    ...

def task_detail_blogger_keyboard(task_id: int) -> InlineKeyboardMarkup:
    ...

def my_task_blogger_keyboard(
    app_id: int, status: str, has_bonus_views: bool = False,
    has_bonus_repeats: bool = False,
) -> InlineKeyboardMarkup:
    ...

# === Заказчик ===

def customer_dashboard_keyboard() -> InlineKeyboardMarkup:
    ...

def payment_type_keyboard() -> InlineKeyboardMarkup:
    ...

def blogger_size_keyboard() -> InlineKeyboardMarkup:
    ...

COUNTRIES = [
    ("🇷🇺 Россия", "Россия"),
    ("🇰🇿 Казахстан", "Казахстан"),
    ("🇧🇾 Беларусь", "Беларусь"),
    ("🇦🇲 Армения", "Армения"),
    ("🇬🇪 Грузия", "Грузия"),
    ("🇹🇯 Таджикистан", "Таджикистан"),
    ("🇺🇿 Узбекистан", "Узбекистан"),
    ("🇰🇬 Кыргызстан", "Кыргызстан"),
    ("🇦🇿 Азербайджан", "Азербайджан"),
    ("🇲🇩 Молдова", "Молдова"),
    ("🇹🇷 Турция", "Турция"),
]


def country_keyboard() -> InlineKeyboardMarkup:
    ...

def blogger_country_keyboard(back_target: str | None = None) -> InlineKeyboardMarkup:
    ...

def customer_country_keyboard(back_target: str | None = None) -> InlineKeyboardMarkup:
    ...

def platforms_select_keyboard(
    selected: list[str] | None = None,
) -> InlineKeyboardMarkup:
    ...

def task_type_keyboard() -> InlineKeyboardMarkup:
    ...

def task_subcategory_keyboard(task_type: str) -> InlineKeyboardMarkup:
    ...

def review_rating_keyboard(report_id: int) -> InlineKeyboardMarkup:
    ...

def pricing_options_keyboard(
    selected: list[str] | None = None,
) -> InlineKeyboardMarkup:
    ...

def confirm_keyboard(yes_cb: str, no_cb: str) -> InlineKeyboardMarkup:
    ...

def customer_task_keyboard(task_id: int, status: str) -> InlineKeyboardMarkup:
    ...

def verify_report_keyboard(report_id: int) -> InlineKeyboardMarkup:
    ...

# === Админ ===

def admin_panel_keyboard() -> InlineKeyboardMarkup:
    ...

def admin_moderate_task_keyboard(task_id: int) -> InlineKeyboardMarkup:
    ...

# === Баланс ===

def balance_keyboard(role: str) -> InlineKeyboardMarkup:
    ...
