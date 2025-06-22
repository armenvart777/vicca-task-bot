from __future__ import annotations

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, Message

import asyncpg
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.queries.blogger_profiles import (
    increment_completed,
    update_blogger_balance,
    update_blogger_rating,
)
from db.queries.reviews import create_review
from db.queries.task_applications import get_application, update_application_status
from db.queries.task_reports import (
    get_pending_reports_for_customer,
    get_report,
    update_report_status,
)
from db.queries.tasks import get_task
from db.queries.transactions import create_transaction
from keyboards.callbacks import CustomerDashCB, ReviewRatingCB, VerifyReportCB
from keyboards.inline import (
    customer_dashboard_keyboard,
    review_rating_keyboard,
    verify_report_keyboard,
)
from services.notifications import notify_user
from states.common_states import ReviewStates
from utils.formatting import format_platform, format_price

router = Router(name="customer_verify_report")


@router.callback_query(CustomerDashCB.filter(F.action == "verify"))
async def show_pending_reports(
    callback: CallbackQuery,
    pool: asyncpg.Pool,
    customer_profile: asyncpg.Record | None,
):
    ...

@router.callback_query(VerifyReportCB.filter(F.action == "view"))
async def view_report(
    callback: CallbackQuery,
    callback_data: VerifyReportCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(VerifyReportCB.filter(F.action == "approve"))
async def approve_report(
    callback: CallbackQuery,
    callback_data: VerifyReportCB,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
    state: FSMContext,
):
    ...

@router.callback_query(VerifyReportCB.filter(F.action == "reject"))
async def reject_report(
    callback: CallbackQuery,
    callback_data: VerifyReportCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(ReviewStates.waiting_rating, ReviewRatingCB.filter())
async def process_review_rating(
    callback: CallbackQuery,
    callback_data: ReviewRatingCB,
    state: FSMContext,
):
    ...

@router.message(ReviewStates.waiting_comment)
async def process_review_comment(
    message: Message,
    state: FSMContext,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
):
    ...
