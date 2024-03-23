from keyboards.default.all import menu, number
from keyboards.inline.all import private_button
from loader import bot, db, dp
from states.rekStates import DelUser, Number
from utils.misc import subscription
import asyncpg
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import BoundFilter, CommandStart


class IsGroup(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP,
        )


class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE


@dp.message_handler(text="Malumotlarim / Малумотларим")
async def profile(message: types.Message):
    get_data = await db.get_user(telegram_id=message.from_user.id)
    user_data = get_data[0]
    await message.answer(f"""
    Ismingiz : {user_data[1]}\n\nRaqamingiz : {user_data[3]}\nTaklif qilgan do'stlaringiz soni: {user_data[4]}\n
----------------------------
Исмингиз : {user_data[1]}\nРақамингиз : {user_data[3]}\nТаклиф қилган дўстларингиз coни: {user_data[4]}
    """, reply_markup=private_button)


@dp.message_handler(text="Bot haqida / Бот ҳақида")
async def about(message: types.Message):
    elements = await db.get_elements()
    bot_username = (await bot.get_me()).username

    await message.answer(f"""
    {elements[0][4]}
    \n\nhttps://t.me/{bot_username}?start={message.from_user.id}    
    """)
