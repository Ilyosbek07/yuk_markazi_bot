from aiogram import types

from data.config import ADMINS
from loader import db, dp


@dp.message_handler(text="dropppp_req")
async def drop_req(message: types.Message):
    await db.drop_requested_users()
    await db.create_table_requested_users()
    await message.answer("Done ✅")


@dp.message_handler(text="dropppp_req_ch")
async def drop_req(message: types.Message):
    await db.drop_req_j_Chanel()
    await db.create_table_request_join_chanel()
    await message.answer("Done ✅")


@dp.message_handler(text="dropppp_users")
async def drop_users(message: types.Message):
    await db.drop_users()
    await db.create_table_users()
    await message.answer("Done ✅")


@dp.message_handler(text="dropppp_tests")
async def drop_tests(message: types.Message):
    await db.drop_test()
    await db.create_table_tests()
    await message.answer("Done ✅")
