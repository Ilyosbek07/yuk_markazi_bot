from aiogram import executor

import filters
import handlers
import middlewares
from handlers.users import start
from loader import bot, db, dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

# from apscheduler.schedulers.asyncio import AsyncIOScheduler


async def on_startup(dispatcher):
    await db.create()
    await db.drop_orders()
    await db.create_orders()
    await db.create_table_tests()
    await db.create_table_chanel()
    await db.create_table_users()
    await db.create_table_admins()
    await db.create_table_add_list()
    await db.create_table_chanel_element()
    await db.create_table_requested_users()
    await db.create_table_add_list_chanel()
    await db.create_table_request_join_chanel()
    await set_default_commands(dispatcher)

    await bot.delete_webhook()
    # scheduler = AsyncIOScheduler(timezone='Asia/Tashkent')

    # scheduler.add_job(start.send, trigger='interval', seconds=60, kwargs={'bot': Bot})
    # scheduler.add_job(start.jsonn, trigger='interval', days=11)
    # scheduler.start()
    admins = await db.select_all_admins()
    try:
        if 935795577 == admins[0][1]:
            print(">>> qo`shilgan")
            print(f">>> Hozirgi adminlar - {admins}")
    except Exception as err:
        print(err)
        await db.add_admin(telegram_id=935795577)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
