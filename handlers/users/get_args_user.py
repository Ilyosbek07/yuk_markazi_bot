import asyncio
from aiogram import types
from loader import db, dp
from data.config import ADMINS
from states.rekStates import RekData
from aiogram.dispatcher import FSMContext
from keyboards.default.rekKeyboards import admin_key, back


@dp.message_handler(text="get", user_id=ADMINS)
async def get_users_args(message: types.Message):
    admins = await db.select_all_admins()
    admins_list = []
    for i in admins:
        admins_list.append(i[1])
    if message.from_user.id in admins_list:
        await message.answer("<b>Id ni Yuboring</b>", reply_markup=back)
        await RekData.get_users_args_state.set()


@dp.message_handler(state=RekData.get_users_args_state)
async def get_all_users_args(message: types.Message, state: FSMContext):
    try:
        if message.text == "🔙️ Orqaga":
            await message.answer("Bekor qilindi", reply_markup=admin_key)
            await state.finish()
        else:
            int(message.text)
            await message.answer("Iltimos biroz kuting", reply_markup=types.ReplyKeyboardRemove())
            all_args_users = await db.get_all_args_users(user_args=message.text)
            if all_args_users == []:
                await message.answer("Hech qanday foydalanuvchi topilmadi")
                await state.finish()
            counter = 0
            max_display_count = 30
            for i in all_args_users:
                counter += 1
                await message.answer(
                    f'Ismi: <a href="https://t.me/{i[2]}">{i[1]}</a>. Id: {i[6]}\n' f"Raqami: {i[3]}\n\n"
                )
                if counter == max_display_count:
                    counter = 0
                await asyncio.sleep(0.05)
            await message.answer(f"Jami: {counter} ta", reply_markup=admin_key)
            await state.finish()
    except Exception as err:
        await message.answer("Faqat son qabul qilinadi\n\nQayta kiriting")
