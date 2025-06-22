from __future__ import annotations

import asyncpg

from db.queries.blogger_profiles import update_blogger_balance
from db.queries.customer_profiles import update_customer_balance
from db.queries.tasks import get_task
from db.queries.transactions import create_transaction


async def reserve_budget(
    pool: asyncpg.Pool, task_id: int, customer_user_id: int, customer_id: int
) -> bool:
    ...

async def release_payment(
    pool: asyncpg.Pool,
    blogger_user_id: int,
    blogger_id: int,
    amount: float,
    task_order: str,
    report_id: int,
) -> float:
    ...

async def refund_escrow(
    pool: asyncpg.Pool, task_id: int, customer_user_id: int, customer_id: int
) -> float:
    ...
