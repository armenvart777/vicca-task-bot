from __future__ import annotations

import asyncpg


PRICING_DEFAULTS = {
    "small": {
        "fix_price": 1000,
        "bonus_views": 1000,
        "views_threshold": 10000,
        "bonus_repeats": 1000,
        "repeats_threshold": 10,
    },
    "medium": {
        "fix_price": 2500,
        "bonus_views": 2500,
        "views_threshold": 20000,
        "bonus_repeats": 2500,
        "repeats_threshold": 20,
    },
    "large": {
        "fix_price": 5000,
        "bonus_views": 5000,
        "views_threshold": 50000,
        "bonus_repeats": 5000,
        "repeats_threshold": 50,
    },
}


async def get_pricing_for_size(pool: asyncpg.Pool, size: str) -> dict:
    ...

def calculate_total_budget(
    pricing: dict, video_limit: int, product_price: float = 0
) -> float:
    ...

def calculate_barter_commission(video_limit: int, commission: float = 300) -> float:
    ...
