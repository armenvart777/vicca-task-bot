from __future__ import annotations

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import asyncpg

from config import settings
from db.queries.users import accept_offer, set_user_role
from keyboards.callbacks import MainMenuCB, OfferCB, RoleSelectCB
from keyboards.inline import (
    blogger_dashboard_keyboard,
    customer_dashboard_keyboard,
    offer_keyboard,
    role_select_keyboard,
)

router = Router(name="start")

WELCOME_TEXT = (
    "VICCA — Ваша экосистема продвижения через механику видео-челленджей.\n\n"
    "Мы объединяем бренды и креаторов в автоматизированной среде "
    "для создания вирального контента и взрывного роста продаж.\n\n"
    "Выберите вашу роль, чтобы продолжить:"
)

OFFER_TEXT = (
    "Прежде чем начать работу, обязательно прочитайте:\n\n"
    "Нажимая «Принимаю», вы подтверждаете согласие с условиями платформы."
)

ABOUT_TEXT = (
    "VICCA — платформа, которая соединяет бренды и блогеров "
    "для создания видео-челленджей.\n\n"
    "Как заказчик — вы создаёте задание на видео, выбираете "
    "категорию блогеров, устанавливаете бюджет. "
    "Блогеры снимают ролики и публикуют их на своих площадках.\n\n"
    "Как блогер — вы находите интересные задания, снимаете видео, "
    "получаете оплату за работу + бонусы за просмотры и челленджи."
)


@router.message(Command("start"))
async def cmd_start(
    message: Message,
    state: FSMContext,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
    blogger_profile: asyncpg.Record | None,
    customer_profile: asyncpg.Record | None,
):
    ...

@router.callback_query(OfferCB.filter(F.action == "agree"))
async def agree_offer(
    callback: CallbackQuery,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
):
    ...

@router.callback_query(RoleSelectCB.filter())
async def select_role(
    callback: CallbackQuery,
    callback_data: RoleSelectCB,
    state: FSMContext,
    pool: asyncpg.Pool,
    user_db: asyncpg.Record,
    blogger_profile: asyncpg.Record | None,
    customer_profile: asyncpg.Record | None,
):
    ...

@router.callback_query(MainMenuCB.filter(F.action == "about"))
async def about_platform(callback: CallbackQuery):
    ...
