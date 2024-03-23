import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.all import menu
from keyboards.default.rekKeyboards import admin_key, back
from loader import db, dp, bot
from states.rekStates import RekData


@dp.callback_query_handler(text="confirm")
async def confirm_order(call: types.CallbackQuery):
    id = call.message.text.split('#')
    await db.confirm_order_status(int(id[0]))
    await call.message.delete_reply_markup()
    await call.message.reply('✅ Tasdiqlangan')


@dp.callback_query_handler(text="cancel")
async def cancel_order(call: types.CallbackQuery):
    id = call.message.text.split('#')
    await db.cancel_order_status(int(id[0]))
    await call.message.delete_reply_markup()
    await call.message.reply('🛑 Bekor qilingan')


@dp.callback_query_handler(text="add_curer")
async def add_curer_to_order(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    message = call.message
    await state.update_data({
        'message': message
    })
    await call.message.answer('👤 Kuryer haqida malumotlarni kiriting.(Ismi Telefon raqami va hk.')
    await RekData.curer.set()


@dp.message_handler(state=RekData.curer)
async def add_curer(msg: types.Message, state: FSMContext):
    await msg.delete()
    data = await state.get_data()
    await msg.answer("🚛 Kuryer malumotlari qo'shildi")
    await msg.answer(f"{data.get('message')}\n\n"
                     f"{msg.text}")
    await state.finish()


@dp.callback_query_handler(text="filling_property")
async def filling_property_answer(call: types.CallbackQuery):
    await call.message.delete()
    elements = await db.get_elements()
    await call.message.answer(elements[0][2])


@dp.message_handler(text="Xabar Yuborish 🗒")
async def bot_start(msg: types.Message):
    admins = await db.select_all_admins()
    admins_list = []
    for i in admins:
        admins_list.append(i[1])
    if msg.from_user.id in admins_list:
        await msg.answer("<b>Xabarni ni yuboring</b>", reply_markup=back)
        await RekData.choice.set()


@dp.message_handler(content_types=["video", "audio", "voice", "photo", "document", "text"], state=RekData.choice)
async def contumum(msg: types.Message, state: FSMContext):
    if msg.text == "🔙️ Orqaga":
        await msg.answer("Bekor qilindi", reply_markup=admin_key)
        await state.finish()

    elif msg.video or msg.audio or msg.voice or msg.document or msg.photo or msg.text:
        if msg.text == "Xabar Yuborish 🗒":
            await msg.answer("Adashdingiz Shekilli\n\n" "To`g`ri ma`lumot kirting")
        else:
            await state.finish()

            users = await db.select_all_users()
            count_baza = await db.count_users()
            count_err = 0
            count = 0
            for user in users:
                user_id = user[6]
                try:
                    await msg.send_copy(chat_id=user_id)
                    count += 1
                    await asyncio.sleep(0.05)
                except Exception as err:
                    count_err += 1
                    await asyncio.sleep(0.05)
                    continue

            await msg.answer(
                f"Yuborilganlar: <b>{count}</b> та."
                f"\n\nYuborilmaganlar: <b>{count_err}</b> та."
                f"\n\nBazada jami: <b>{count_baza}</b> та"
                f" foydalanuvchi mavjud.",
                reply_markup=admin_key,
            )


@dp.message_handler(state="*")
async def back_all(message: types.Message, state: FSMContext):
    if message.text == "Back":
        await message.answer(text="Bosh menu", reply_markup=menu)
        await state.finish()
