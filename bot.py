from __future__ import annotations

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from config import settings
from db.engine import close_pool, init_db
from middlewares.db_middleware import DbMiddleware
from middlewares.role_middleware import RoleMiddleware
from middlewares.throttle_middleware import ThrottleMiddleware
from middlewares.user_middleware import UserMiddleware

# Handlers
from handlers.admin.panel import router as admin_panel_router
from handlers.admin.moderation import router as admin_moderation_router
from handlers.admin.users_mgmt import router as admin_users_router
from handlers.admin.tasks_mgmt import router as admin_tasks_router
from handlers.admin.broadcast import router as admin_broadcast_router
from handlers.admin.categories_mgmt import router as admin_categories_router
from handlers.admin.settings import router as admin_settings_router
from handlers.admin.reports_mgmt import router as admin_reports_router
from handlers.admin.payments_mgmt import router as admin_payments_router

from handlers.blogger.edit_profile import router as blogger_edit_router
from handlers.blogger.registration import router as blogger_reg_router
from handlers.blogger.dashboard import router as blogger_dash_router
from handlers.blogger.find_tasks import router as blogger_find_router
from handlers.blogger.my_tasks import router as blogger_my_tasks_router
from handlers.blogger.submit_report import router as blogger_report_router
from handlers.blogger.balance import router as blogger_balance_router

from handlers.customer.registration import router as customer_reg_router
from handlers.customer.dashboard import router as customer_dash_router
from handlers.customer.create_task import router as customer_create_router
from handlers.customer.my_tasks import router as customer_my_tasks_router
from handlers.customer.verify_report import router as customer_verify_router
from handlers.customer.balance import router as customer_balance_router

from handlers.start import router as start_router
from handlers.common.menu import router as menu_router
from handlers.common.profile import router as profile_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


async def main():
    ...

if __name__ == "__main__":
    asyncio.run(main())
