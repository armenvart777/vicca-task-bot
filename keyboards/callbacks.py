from __future__ import annotations

from aiogram.filters.callback_data import CallbackData


# === Общие ===
class MainMenuCB(CallbackData, prefix="menu"):
    action: str


class OfferCB(CallbackData, prefix="offer"):
    action: str = "agree"


class RoleSelectCB(CallbackData, prefix="role"):
    role: str


class ProfileCB(CallbackData, prefix="prof"):
    action: str


class PaginationCB(CallbackData, prefix="page"):
    target: str
    page: int


# === Блогер ===
class BloggerDashCB(CallbackData, prefix="bdash"):
    action: str


class RegBackCB(CallbackData, prefix="regback"):
    """Кнопка Назад в регистрации/редактировании профиля."""
    target: str  # "blogger" / "customer" / "edit_blogger"


class BarterCB(CallbackData, prefix="barter"):
    value: str  # "yes" / "no"


class BloggerPlatformCB(CallbackData, prefix="bplat"):
    platform: str
    action: str = "select"


class TaskBrowseCB(CallbackData, prefix="tbrowse"):
    id: int = 0
    action: str = "list"


class TaskCategoryCB(CallbackData, prefix="tcat"):
    id: int
    action: str = "filter"


class MyTaskCB(CallbackData, prefix="mytask"):
    id: int
    action: str = "view"


class ReportCB(CallbackData, prefix="report"):
    id: int
    action: str = "view"


# === Заказчик ===
class CustomerDashCB(CallbackData, prefix="cdash"):
    action: str


class CustomerTaskCB(CallbackData, prefix="ctask"):
    id: int
    action: str = "view"


class VerifyReportCB(CallbackData, prefix="vreport"):
    id: int
    action: str


class TaskPaymentCB(CallbackData, prefix="tpay"):
    id: int
    action: str = "pay"


class PaymentTypeCB(CallbackData, prefix="paytype"):
    type: str


class BloggerSizeCB(CallbackData, prefix="bsize"):
    size: str


class CountryCB(CallbackData, prefix="country"):
    country: str


class BloggerCountryCB(CallbackData, prefix="bcountry"):
    country: str


class CustomerCountryCB(CallbackData, prefix="ccountry"):
    country: str


class PlatformSelectCB(CallbackData, prefix="platsel"):
    platform: str
    action: str = "toggle"


class TaskTypeCB(CallbackData, prefix="ttype"):
    type: str  # "business" or "product"


class TaskSubcategoryCB(CallbackData, prefix="tsubcat"):
    name: str


class ReviewRatingCB(CallbackData, prefix="revrate"):
    report_id: int
    rating: int


class PricingOptionCB(CallbackData, prefix="propt"):
    option: str  # "fix" / "bonus_views" / "bonus_repeats"
    action: str = "toggle"  # "toggle" / "done"


# === Админ ===
class AdminPanelCB(CallbackData, prefix="apanel"):
    section: str


class AdminModerateCB(CallbackData, prefix="amod"):
    id: int
    action: str


class AdminUserCB(CallbackData, prefix="auser"):
    id: int
    action: str


class AdminTaskCB(CallbackData, prefix="atask"):
    id: int
    action: str


class AdminCategoryCB(CallbackData, prefix="acat"):
    id: int
    action: str


class AdminSettingCB(CallbackData, prefix="aset"):
    key: str
    action: str = "edit"


class AdminConfirmCB(CallbackData, prefix="aconf"):
    action: str
    target: str = ""
    target_id: int = 0


class BroadcastAudienceCB(CallbackData, prefix="bcast"):
    audience: str  # "all" / "bloggers" / "customers"


class AdminBloggerCB(CallbackData, prefix="ablog"):
    id: int
    action: str = "view"


class AdminCustomerCB(CallbackData, prefix="acust"):
    id: int
    action: str = "view"


class AdminReportCB(CallbackData, prefix="arep"):
    id: int
    action: str = "view"


# === Баланс ===
class BalanceCB(CallbackData, prefix="bal"):
    action: str
    role: str = ""


class PayMethodCB(CallbackData, prefix="paymethod"):
    method: str  # "sbp" or "card"


class AdminPayRequestCB(CallbackData, prefix="apreq"):
    id: int
    action: str = "view"  # "view", "approve", "reject"
