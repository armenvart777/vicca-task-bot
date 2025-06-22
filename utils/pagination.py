from __future__ import annotations

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboards.callbacks import PaginationCB


def paginate(
    items: list, page: int, per_page: int = 8
) -> tuple[list, int, bool, bool]:
    ...

def add_pagination_row(
    builder: InlineKeyboardBuilder,
    page: int,
    total_pages: int,
    has_prev: bool,
    has_next: bool,
    target: str,
) -> None:
    ...
