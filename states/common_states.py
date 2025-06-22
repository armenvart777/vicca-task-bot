from __future__ import annotations

from aiogram.fsm.state import State, StatesGroup


class EditProfileStates(StatesGroup):
    choosing_field = State()
    waiting_value = State()


class TopupStates(StatesGroup):
    waiting_amount = State()
    waiting_method = State()
    waiting_confirmation = State()
    waiting_payment = State()


class WithdrawalStates(StatesGroup):
    waiting_amount = State()
    waiting_sbp_details = State()
    confirming = State()


class ReviewStates(StatesGroup):
    waiting_rating = State()
    waiting_comment = State()


class SupportStates(StatesGroup):
    waiting_message = State()
