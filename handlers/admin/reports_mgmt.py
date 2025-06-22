from __future__ import annotations

from aiogram import F, Router
from aiogram.types import CallbackQuery, InlineKeyboardButton

import asyncpg
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.queries.statistics import get_pending_reports_admin, get_recent_reports
from db.queries.task_reports import get_report, update_report_status
from db.queries.task_applications import get_application, update_application_status
from db.queries.tasks import get_task
from db.queries.blogger_profiles import update_blogger_balance, increment_completed
from db.queries.transactions import create_transaction
from filters.admin_filter import IsAdmin
from keyboards.callbacks import AdminPanelCB, AdminReportCB
from services.notifications import notify_user
from utils.formatting import format_price

router = Router(name="admin_reports")
router.callback_query.filter(IsAdmin())


@router.callback_query(AdminPanelCB.filter(F.section == "reports"))
async def reports_menu(callback: CallbackQuery):
    ...

@router.callback_query(AdminPanelCB.filter(F.section == "reports_pending"))
async def pending_reports(callback: CallbackQuery, pool: asyncpg.Pool):
    ...

@router.callback_query(AdminPanelCB.filter(F.section == "reports_recent"))
async def recent_reports_list(callback: CallbackQuery, pool: asyncpg.Pool):
    ...

@router.callback_query(AdminReportCB.filter(F.action == "view"))
async def view_report(
    callback: CallbackQuery,
    callback_data: AdminReportCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(AdminReportCB.filter(F.action == "show_file"))
async def show_report_file(
    callback: CallbackQuery,
    callback_data: AdminReportCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(AdminReportCB.filter(F.action == "approve"))
async def approve_report_admin(
    callback: CallbackQuery,
    callback_data: AdminReportCB,
    pool: asyncpg.Pool,
):
    ...

@router.callback_query(AdminReportCB.filter(F.action == "reject"))
async def reject_report_admin(
    callback: CallbackQuery,
    callback_data: AdminReportCB,
    pool: asyncpg.Pool,
):
    ...
