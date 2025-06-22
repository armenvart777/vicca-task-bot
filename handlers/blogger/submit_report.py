from __future__ import annotations

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import asyncpg

from db.queries.task_applications import get_application, update_application_status
from db.queries.task_reports import create_report, get_reports_by_application
from db.queries.tasks import get_task
from keyboards.callbacks import MyTaskCB
from keyboards.inline import blogger_dashboard_keyboard, my_task_blogger_keyboard
from services.notifications import notify_user
from states.blogger_states import BonusReport, SubmitReport
from utils.formatting import format_platform, format_price
from utils.validators import validate_url

router = Router(name="blogger_submit_report")


# ========================== Основной отчёт ==========================

@router.callback_query(MyTaskCB.filter(F.action == "submit"))
async def start_submit(
    callback: CallbackQuery,
    callback_data: MyTaskCB,
    state: FSMContext,
):
    ...

@router.message(SubmitReport.waiting_video_link)
async def process_video_link(message: Message, state: FSMContext):
    ...

@router.message(SubmitReport.waiting_platform)
async def process_platform(message: Message, state: FSMContext):
    ...

@router.message(SubmitReport.waiting_comment)
async def process_comment(message: Message, state: FSMContext):
    ...

@router.message(SubmitReport.waiting_stats_file)
async def process_stats_file(message: Message, state: FSMContext):
    ...

@router.message(SubmitReport.confirming)
async def confirm_report(
    message: Message,
    state: FSMContext,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
):
    ...

# =================== Бонусный отчёт (просмотры / челленджи) ===================

@router.callback_query(MyTaskCB.filter(F.action == "bonus_views"))
async def start_bonus_views(
    callback: CallbackQuery,
    callback_data: MyTaskCB,
    state: FSMContext,
):
    ...

@router.callback_query(MyTaskCB.filter(F.action == "bonus_repeats"))
async def start_bonus_repeats(
    callback: CallbackQuery,
    callback_data: MyTaskCB,
    state: FSMContext,
):
    ...

@router.message(BonusReport.waiting_proof_link)
async def bonus_proof_link(message: Message, state: FSMContext):
    ...

@router.message(BonusReport.waiting_proof_file)
async def bonus_proof_file(message: Message, state: FSMContext):
    ...

@router.message(BonusReport.confirming)
async def confirm_bonus_report(
    message: Message,
    state: FSMContext,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
):
    ...
