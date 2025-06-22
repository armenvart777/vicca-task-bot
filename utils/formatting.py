from __future__ import annotations

from decimal import Decimal


def format_price(amount: float | Decimal) -> str:
    ...

def format_rating(rating: float | Decimal) -> str:
    ...

def format_blogger_size(size: str) -> str:
    ...

def format_payment_type(ptype: str) -> str:
    ...

def format_status(status: str) -> str:
    ...

PLATFORM_NAMES = {
    "youtube": "YouTube",
    "tiktok": "TikTok",
    "instagram": "Instagram",
    "vk": "ВКонтакте",
    "wibes": "WiBES",
}


def format_platform(platform: str) -> str:
    ...

def format_platforms_list(platforms: list[str]) -> str:
    ...
