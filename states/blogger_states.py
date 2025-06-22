from __future__ import annotations

from aiogram.fsm.state import State, StatesGroup


class BloggerRegistration(StatesGroup):
    waiting_name = State()
    waiting_city = State()
    waiting_phone = State()
    waiting_country = State()
    waiting_barter = State()
    waiting_platforms = State()
    waiting_platform_link = State()
    waiting_platform_subscribers = State()
    waiting_more_platforms = State()
    confirming = State()


class BloggerEditProfile(StatesGroup):
    waiting_name = State()
    waiting_city = State()
    waiting_phone = State()
    waiting_country = State()
    waiting_barter = State()
    waiting_platforms = State()
    waiting_platform_link = State()
    waiting_platform_subscribers = State()
    confirming = State()


class SubmitReport(StatesGroup):
    waiting_video_link = State()
    waiting_platform = State()
    waiting_comment = State()
    waiting_stats_file = State()
    confirming = State()


class BonusReport(StatesGroup):
    waiting_type = State()
    waiting_proof_link = State()
    waiting_proof_file = State()
    confirming = State()
