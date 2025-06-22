from __future__ import annotations

from aiogram.fsm.state import State, StatesGroup


class AdminModerationStates(StatesGroup):
    waiting_reject_reason = State()


class AdminBroadcastStates(StatesGroup):
    waiting_audience = State()
    waiting_message = State()
    confirming = State()


class AdminUserSearchStates(StatesGroup):
    waiting_query = State()


class AdminCategoryStates(StatesGroup):
    waiting_name = State()
    waiting_emoji = State()


class AdminSettingsStates(StatesGroup):
    waiting_value = State()
