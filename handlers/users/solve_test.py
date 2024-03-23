import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

from keyboards.default.all import menu
from loader import bot, db, dp
from states.rekStates import RekData, SolveTestState


@dp.message_handler(text=f"test")
async def to_user(message: types.Message):
    await message.answer("Id ni yuboring")
    await RekData.send_user.set()


@dp.message_handler(state=RekData.send_user)
async def to_user_test(message: types.Message, state: FSMContext):
    text = (
        "<b>⚡️ Loyiha doirasida yangi testlar botga qo’shildi</b>\n\n"
        "🗒 Testlarni yechish uchun pastdagi tugmani bosing"
    )
    markup_to_user = InlineKeyboardMarkup(row_width=1)

    markup_to_user.insert(InlineKeyboardButton(text="✍️ Boshlash", callback_data=f"new_test"))
    try:
        await bot.send_message(chat_id=message.text, text=text, reply_markup=markup_to_user)
    except Exception as err:
        pass
    await state.finish()


@dp.callback_query_handler(text=f"new_test")
async def checker(call: types.CallbackQuery):
    await call.message.delete()
    date = datetime.date.today()
    tests = await db.get_tests()
    counter = 0
    markup_to_user = types.ReplyKeyboardMarkup(row_width=1)
    if len(tests) > 4:
        for i in tests[0]:
            if counter == 6:
                break
            elif counter > 1:
                answer = i.split("-")
                markup_to_user.add(types.KeyboardButton(text=f"{answer[0]}"))
            counter += 1

        await call.message.answer(text=f"{tests[0]['question']}", reply_markup=markup_to_user)
        await SolveTestState.a1.set()
    else:
        await call.message.answer("Savollar mavjud emas")


@dp.message_handler(state=SolveTestState.a1)
async def check_a1(message: types.Message, state: FSMContext):
    await state.update_data({"user_answer_1": message.text})
    date = datetime.date.today()
    tests = await db.get_tests()
    counter = 0
    markup_to_user = types.ReplyKeyboardMarkup(row_width=1)
    for i in tests[1]:
        if counter == 6:
            break
        elif counter > 1:
            answer = i.split("-")
            markup_to_user.insert(types.KeyboardButton(text=answer[0]))

        counter += 1

    await message.answer(text=f"{tests[1]['question']}", reply_markup=markup_to_user)
    await SolveTestState.a2.set()


@dp.message_handler(state=SolveTestState.a2)
async def check_a_2(message: types.Message, state: FSMContext):
    await state.update_data({"user_answer_2": message.text})
    date = datetime.date.today()
    tests = await db.get_tests()
    counter = 0
    markup_to_user = types.ReplyKeyboardMarkup(row_width=1)

    for i in tests[2]:
        if counter == 6:
            break
        elif counter > 1:
            answer = i.split("-")
            markup_to_user.insert(types.KeyboardButton(text=answer[0]))
        counter += 1

    await message.answer(text=f"{tests[2]['question']}", reply_markup=markup_to_user)
    await SolveTestState.a3.set()


@dp.message_handler(state=SolveTestState.a3)
async def check_a_3(message: types.Message, state: FSMContext):
    await state.update_data({"user_answer_3": message.text})
    date = datetime.date.today()
    tests = await db.get_tests()
    counter = 0
    markup_to_user = types.ReplyKeyboardMarkup(row_width=1)

    for i in tests[3]:
        if counter == 6:
            break
        elif counter > 1:
            answer = i.split("-")
            markup_to_user.insert(types.KeyboardButton(text=answer[0]))
        counter += 1

    await message.answer(text=f"{tests[3]['question']}", reply_markup=markup_to_user)
    await SolveTestState.a4.set()


@dp.message_handler(state=SolveTestState.a4)
async def check_a_4(message: types.Message, state: FSMContext):
    await state.update_data({"user_answer_4": message.text})
    date = datetime.date.today()
    tests = await db.get_tests()
    counter = 0
    markup_to_user = types.ReplyKeyboardMarkup(row_width=1)

    for i in tests[4]:
        if counter == 6:
            break
        elif counter > 1:
            answer = i.split("-")
            markup_to_user.insert(types.KeyboardButton(text=answer[0]))
        counter += 1

    await message.answer(text=f"{tests[4]['question']}", reply_markup=markup_to_user)
    await SolveTestState.check.set()


@dp.message_handler(state=SolveTestState.check)
async def check(message: types.Message, state: FSMContext):
    await state.update_data({"user_answer_5": message.text})
    date = datetime.date.today()
    tests = await db.get_tests()
    data = await state.get_data()
    user_answer_1 = data.get("user_answer_1")
    user_answer_2 = data.get("user_answer_2")
    user_answer_3 = data.get("user_answer_3")
    user_answer_4 = data.get("user_answer_4")
    user_answer_5 = data.get("user_answer_5")

    answers = {}
    counter = 1
    for test in tests:
        answers[f"{test[2].split('-')[1]}_{counter}"] = test[2].split("-")[0]
        answers[f"{test[3].split('-')[1]}_{counter}"] = test[3].split("-")[0]
        answers[f"{test[4].split('-')[1]}_{counter}"] = test[4].split("-")[0]
        answers[f"{test[5].split('-')[1]}_{counter}"] = test[5].split("-")[0]
        answers[f"{test[6].split('-')[1]}_{counter}"] = test[6].split("-")[0]
        counter += 1
    result_1 = "✅" if user_answer_1 == answers["t_1"].replace("\n", "") else "🚫"
    result_2 = "✅" if user_answer_2 == answers["t_2"].replace("\n", "") else "🚫"
    result_3 = "✅" if user_answer_3 == answers["t_3"].replace("\n", "") else "🚫"
    result_4 = "✅" if user_answer_4 == answers["t_4"].replace("\n", "") else "🚫"
    result_5 = "✅" if user_answer_5 == answers["t_5"].replace("\n", "") else "🚫"
    counter = 0
    if result_1 == "✅":
        counter += 1
    if result_2 == "✅":
        counter += 1
    if result_3 == "✅":
        counter += 1
    if result_4 == "✅":
        counter += 1
    if result_5 == "✅":
        counter += 1
    user = await db.get_user(telegram_id=message.from_user.id)
    user_score = 0
    if user:
        user_score += user[0]["score"]
    else:
        await db.add_user(
            full_name=message.from_user.full_name, username=message.from_user.username, telegram_id=message.from_user.id
        )
    if counter != 0:
        user_score += counter * 3
    await db.update_user_score(score=user_score, telegram_id=message.from_user.id)
    text = (
        f"<b>📊 Natijalaringiz</b>\n\n"
        f"1.{result_1}\n"
        f"2.{result_2}\n"
        f"3.{result_3}\n"
        f"4.{result_4}\n"
        f"5.{result_5}"
    )

    if counter == 0:
        await message.answer(f"{text}\n\n" f"Afsus siz to'g'ri javoblarni topa olmadingiz", reply_markup=menu)
        await state.finish()
    else:
        text += (
            f"\n\nSiz {counter} ta savolga to’g’ri javob topdingiz\n\n"
            f"Sizga {counter * 3} ball taqdim qilindi\n\n"
            f"Hozirda sizda {user_score} ball mavjud"
        )
        await message.answer(text, reply_markup=menu)
    await state.finish()
