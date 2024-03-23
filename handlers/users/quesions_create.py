import asyncio
import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)

from keyboards.default.rekKeyboards import admin_key
from loader import bot, db, dp
from states.rekStates import QuestionsState


@dp.message_handler(text="senddd")
async def admin_answer(message: types.Message, state: FSMContext):
    await message.answer(
        "Test Yuborish boshlandi\n\n" "Iltimos jarayon tugaguncha botdan foydalanmang",
        reply_markup=types.ReplyKeyboardRemove(),
    )
    users = await db.select_all_users()
    text = (
        "<b>⚡️ Loyiha doirasida yangi testlar botga qo’shildi</b>\n\n"
        "🗒 Testlarni yechish uchun pastdagi tugmani bosing"
    )
    markup_to_user = InlineKeyboardMarkup(row_width=1)

    markup_to_user.insert(InlineKeyboardButton(text="✍️ Boshlash", callback_data=f"new_test"))
    counter = 0
    bad_counter = 0
    for user in users:
        if user["telegram_id"] == 6610230337 or 5870181165:
            counter
        try:
            await bot.send_message(chat_id=user["telegram_id"], text=text, reply_markup=markup_to_user)
            counter += 1
            await asyncio.sleep(0.05)
        except Exception as err:
            bad_counter += 1
            await asyncio.sleep(0.05)
    await message.answer(f"Test yuborish yakunlandi\nTest yuborilganlar:{counter}\n" f"Yuborilmaganlar:{bad_counter}")
    await state.finish()


@dp.message_handler(text="Test qo'shish")
async def test_create(message: types.Message):
    admins = await db.select_all_admins()
    admins_list = []
    for i in admins:
        admins_list.append(i[1])
    if message.from_user.id in admins_list:
        tests = await db.get_tests()
        if tests:
            await message.answer(
                "Bazada testlar mavjud\n"
                "Yangi qo'shish uchun avvalgilarini ochiring\n\n"
                "O`chirish uchun botga <b>dropppp_tests</b> deb yozing yuboring va qaytadan"
                "<b>Test qo'shish </b> tugmasini bosing"
            )
        else:
            await message.answer("1-Savolni kiriting", reply_markup=types.ReplyKeyboardRemove())
            await QuestionsState.a1.set()


@dp.message_handler(state=QuestionsState.a1)
async def question_answers_1(message: types.Message, state: FSMContext):
    if message.text == "/start":
        await state.finish()
        await message.answer("Admin qism", reply_markup=admin_key)
    await state.update_data({"question_1": message.text})
    await message.answer(
        "1-Savol uchun javoblarni \n\n"
        "Variant-f,\n"
        "Variant-f,\n"
        "Variant-t,\n"
        "Variant-f,\n\n"
        "formata kiriting 👆 (javoblar , orqali ajratib olinadi, f - false, t- true)"
    )
    await QuestionsState.q2.set()


@dp.message_handler(state=QuestionsState.q2)
async def question_2(message: types.Message, state: FSMContext):
    if message.text == "/start":
        await state.finish()
        await message.answer("Admin qism", reply_markup=admin_key)

    answers = message.text.split(",")

    await state.update_data(
        {
            "question_1_answer_1": answers[0],
            "question_1_answer_2": answers[1],
            "question_1_answer_3": answers[2],
            "question_1_answer_4": answers[3],
        }
    )
    await message.answer("Qabul qilindi")
    await message.answer("2-Savolni kiriting")
    await QuestionsState.a2.set()


@dp.message_handler(state=QuestionsState.a2)
async def question_answers_2(message: types.Message, state: FSMContext):
    if message.text == "/start":
        await state.finish()
        await message.answer("Admin qism", reply_markup=admin_key)

    await state.update_data({"question_2": message.text})
    await message.answer(
        "2-Savol uchun javoblarni \n\n"
        "Variant-f,\n"
        "Variant-f,\n"
        "Variant-t,\n"
        "Variant-f,\n\n"
        "formata kiriting 👆 (javoblar , orqali ajratib olinadi, f - false, t- true)"
    )
    await QuestionsState.q3.set()


@dp.message_handler(state=QuestionsState.q3)
async def question_3(message: types.Message, state: FSMContext):
    if message.text == "/start":
        await state.finish()
        await message.answer("Admin qism", reply_markup=admin_key)

    answers = message.text.split(",")

    await state.update_data(
        {
            "question_2_answer_1": answers[0],
            "question_2_answer_2": answers[1],
            "question_2_answer_3": answers[2],
            "question_2_answer_4": answers[3],
        }
    )
    await message.answer("Qabul qilindi")
    await message.answer("3-Savolni kiriting")
    await QuestionsState.a3.set()


@dp.message_handler(state=QuestionsState.a3)
async def question_answers_3(message: types.Message, state: FSMContext):
    if message.text == "/start":
        await state.finish()
        await message.answer("Admin qism", reply_markup=admin_key)

    await state.update_data({"question_3": message.text})
    await message.answer(
        "3-Savol uchun javoblarni \n\n"
        "Variant-f,\n"
        "Variant-f,\n"
        "Variant-t,\n"
        "Variant-f,\n\n"
        "formata kiriting 👆 (javoblar , orqali ajratib olinadi, f - false, t- true)"
    )
    await QuestionsState.q4.set()


@dp.message_handler(state=QuestionsState.q4)
async def question_4(message: types.Message, state: FSMContext):
    if message.text == "/start":
        await state.finish()
        await message.answer("Admin qism", reply_markup=admin_key)

    answers = message.text.split(",")

    await state.update_data(
        {
            "question_3_answer_1": answers[0],
            "question_3_answer_2": answers[1],
            "question_3_answer_3": answers[2],
            "question_3_answer_4": answers[3],
        }
    )
    await message.answer("Qabul qilindi")
    await message.answer("4-Savolni kiriting")
    await QuestionsState.a4.set()


@dp.message_handler(state=QuestionsState.a4)
async def question_answers_4(message: types.Message, state: FSMContext):
    if message.text == "/start":
        await state.finish()
        await message.answer("Admin qism", reply_markup=admin_key)

    await state.update_data({"question_4": message.text})
    await message.answer(
        "4-Savol uchun javoblarni \n\n"
        "Variant-f,\n"
        "Variant-f,\n"
        "Variant-t,\n"
        "Variant-f,\n\n"
        "formata kiriting 👆 (javoblar , orqali ajratib olinadi, f - false, t- true)"
    )
    await QuestionsState.a5.set()


@dp.message_handler(state=QuestionsState.a5)
async def question_5(message: types.Message, state: FSMContext):
    if message.text == "/start":
        await state.finish()
        await message.answer("Admin qism", reply_markup=admin_key)

    answers = message.text.split(",")

    await state.update_data(
        {
            "question_4_answer_1": answers[0],
            "question_4_answer_2": answers[1],
            "question_4_answer_3": answers[2],
            "question_4_answer_4": answers[3],
        }
    )
    await message.answer("Qabul qilindi")
    await message.answer("5-Savolni kiriting")
    await QuestionsState.q5.set()


@dp.message_handler(state=QuestionsState.q5)
async def question_answers_5(message: types.Message, state: FSMContext):
    if message.text == "/start":
        await state.finish()
        await message.answer("Admin qism", reply_markup=admin_key)

    await state.update_data({"question_5": message.text})
    await message.answer(
        "5-Savol uchun javoblarni \n\n"
        "Variant-f,\n"
        "Variant-f,\n"
        "Variant-t,\n"
        "Variant-f,\n\n"
        "formata kiriting 👆 (javoblar , orqali ajratib olinadi, f - false, t- true)"
    )
    await QuestionsState.check.set()


@dp.message_handler(state=QuestionsState.check)
async def check(message: types.Message, state: FSMContext):
    if message.text == "/start":
        await state.finish()
        await message.answer("Admin qism", reply_markup=admin_key)
    else:
        answers = message.text.split(",")

        await state.update_data(
            {
                "question_5_answer_1": answers[0],
                "question_5_answer_2": answers[1],
                "question_5_answer_3": answers[2],
                "question_5_answer_4": answers[3],
            }
        )
        await message.answer("Qabul qilindi")
        data = await state.get_data()

        question_1 = data.get("question_1")
        question_2 = data.get("question_2")
        question_3 = data.get("question_3")
        question_4 = data.get("question_4")
        question_5 = data.get("question_5")
        questions = [question_1, question_2, question_3, question_4, question_5]
        question_1_answer_1 = data.get("question_1_answer_1")
        question_1_answer_2 = data.get("question_1_answer_2")
        question_1_answer_3 = data.get("question_1_answer_3")
        question_1_answer_4 = data.get("question_1_answer_4")
        questions_1_answer = [question_1_answer_1, question_1_answer_2, question_1_answer_3, question_1_answer_4]

        question_2_answer_1 = data.get("question_2_answer_1")
        question_2_answer_2 = data.get("question_2_answer_2")
        question_2_answer_3 = data.get("question_2_answer_3")
        question_2_answer_4 = data.get("question_2_answer_4")
        questions_2_answer = [question_2_answer_1, question_2_answer_2, question_2_answer_3, question_2_answer_4]

        question_3_answer_1 = data.get("question_3_answer_1")
        question_3_answer_2 = data.get("question_3_answer_2")
        question_3_answer_3 = data.get("question_3_answer_3")
        question_3_answer_4 = data.get("question_3_answer_4")
        questions_3_answer = [question_3_answer_1, question_3_answer_2, question_3_answer_3, question_3_answer_4]

        question_4_answer_1 = data.get("question_4_answer_1")
        question_4_answer_2 = data.get("question_4_answer_2")
        question_4_answer_3 = data.get("question_4_answer_3")
        question_4_answer_4 = data.get("question_4_answer_4")
        questions_4_answer = [question_4_answer_1, question_4_answer_2, question_4_answer_3, question_4_answer_4]

        question_5_answer_1 = data.get("question_5_answer_1")
        question_5_answer_2 = data.get("question_5_answer_2")
        question_5_answer_3 = data.get("question_5_answer_3")
        question_5_answer_4 = data.get("question_5_answer_4")
        questions_5_answer = [question_5_answer_1, question_5_answer_2, question_5_answer_3, question_5_answer_4]

        markup = InlineKeyboardMarkup(row_width=1)
        markup_2 = InlineKeyboardMarkup(row_width=1)
        markup_3 = InlineKeyboardMarkup(row_width=1)
        markup_4 = InlineKeyboardMarkup(row_width=1)
        markup_5 = InlineKeyboardMarkup(row_width=1)
        for i in range(5):
            for n in range(4):
                if i == 0:
                    answer = questions_1_answer[n].split("-")
                    markup.insert(InlineKeyboardButton(text=f"{answer[0]}", callback_data=f"{answer[1]}"))
                elif i == 1:
                    answer = questions_2_answer[n].split("-")
                    markup_2.insert(InlineKeyboardButton(text=f"{answer[0]}", callback_data=f"{answer[1]}"))
                elif i == 2:
                    answer = questions_3_answer[n].split("-")
                    markup_3.insert(InlineKeyboardButton(text=f"{answer[0]}", callback_data=f"{answer[1]}"))
                elif i == 3:
                    answer = questions_4_answer[n].split("-")
                    markup_4.insert(InlineKeyboardButton(text=f"{answer[0]}", callback_data=f"{answer[1]}"))
                elif i == 4:
                    answer = questions_5_answer[n].split("-")
                    markup_5.insert(InlineKeyboardButton(text=f"{answer[0]}", callback_data=f"{answer[1]}"))
            if i == 0:
                await message.answer(text=questions[i], reply_markup=markup)
            elif i == 1:
                await message.answer(text=questions[i], reply_markup=markup_2)
            elif i == 2:
                await message.answer(text=questions[i], reply_markup=markup_3)
            elif i == 3:
                await message.answer(text=questions[i], reply_markup=markup_4)
            elif i == 4:
                await message.answer(text=questions[i], reply_markup=markup_5)
        but = ReplyKeyboardMarkup(
            row_width=3,
            resize_keyboard=True,
        )
        but.add(KeyboardButton(text="🗒 Testni Yuborish"))
        but.add(KeyboardButton(text="♻️ Qayta kiritish"))

        await message.answer(
            "Siz kiritgan savollar 👆 \n\n"
            "Hammasi to`g`ri bo`lsa <b>🗒 Testni Yuborish</b> tugmasini bosing\n\n"
            "Biror xatolik ketgan bo`lsa <b>♻️ Qayta kiritish</b> tugmasini bosing\n\n"
            "Bekor qilish uchun /start buyrug`ini yuboring",
            reply_markup=but,
        )
        await QuestionsState.admin_check.set()


@dp.message_handler(state=QuestionsState.admin_check)
async def admin_answer(message: types.Message, state: FSMContext):
    if message.text == "/start":
        await state.reset_data()
        await message.answer("Admin qism", reply_markup=admin_key)
        await state.finish()
    elif message.text == "♻️ Qayta kiritish":
        await state.reset_data()
        await message.answer("1-Savolni kiritin", reply_markup=types.ReplyKeyboardRemove())
        await QuestionsState.a1.set()
    elif message.text == "🗒 Testni Yuborish":
        await message.answer(
            "Test Yuborish boshlandi\n\n" "Iltimos jarayon tugaguncha botdan foydalanmang",
            reply_markup=types.ReplyKeyboardRemove(),
        )
        data = await state.get_data()
        question_1 = data.get("question_1")
        question_2 = data.get("question_2")
        question_3 = data.get("question_3")
        question_4 = data.get("question_4")
        question_5 = data.get("question_5")
        question_1_answer_1 = data.get("question_1_answer_1")
        question_1_answer_2 = data.get("question_1_answer_2")
        question_1_answer_3 = data.get("question_1_answer_3")
        question_1_answer_4 = data.get("question_1_answer_4")

        question_2_answer_1 = data.get("question_2_answer_1")
        question_2_answer_2 = data.get("question_2_answer_2")
        question_2_answer_3 = data.get("question_2_answer_3")
        question_2_answer_4 = data.get("question_2_answer_4")

        question_3_answer_1 = data.get("question_3_answer_1")
        question_3_answer_2 = data.get("question_3_answer_2")
        question_3_answer_3 = data.get("question_3_answer_3")
        question_3_answer_4 = data.get("question_3_answer_4")

        question_4_answer_1 = data.get("question_4_answer_1")
        question_4_answer_2 = data.get("question_4_answer_2")
        question_4_answer_3 = data.get("question_4_answer_3")
        question_4_answer_4 = data.get("question_4_answer_4")

        question_5_answer_1 = data.get("question_5_answer_1")
        question_5_answer_2 = data.get("question_5_answer_2")
        question_5_answer_3 = data.get("question_5_answer_3")
        question_5_answer_4 = data.get("question_5_answer_4")

        questions = [question_1, question_2, question_3, question_4, question_5]

        for i in range(len(questions)):
            if i == 0:
                await db.add_test_question(
                    question=questions[i],
                    answer_1=question_1_answer_1,
                    answer_2=question_1_answer_2,
                    answer_3=question_1_answer_3,
                    answer_4=question_1_answer_4,
                    day=f"{datetime.date.today()}",
                )
            elif i == 1:
                await db.add_test_question(
                    question=questions[i],
                    answer_1=question_2_answer_1,
                    answer_2=question_2_answer_2,
                    answer_3=question_2_answer_3,
                    answer_4=question_2_answer_4,
                    day=f"{datetime.date.today()}",
                )
            elif i == 2:
                await db.add_test_question(
                    question=questions[i],
                    answer_1=question_3_answer_1,
                    answer_2=question_3_answer_2,
                    answer_3=question_3_answer_3,
                    answer_4=question_3_answer_4,
                    day=f"{datetime.date.today()}",
                )
            elif i == 3:
                await db.add_test_question(
                    question=questions[i],
                    answer_1=question_4_answer_1,
                    answer_2=question_4_answer_2,
                    answer_3=question_4_answer_3,
                    answer_4=question_4_answer_4,
                    day=f"{datetime.date.today()}",
                )
            elif i == 4:
                await db.add_test_question(
                    question=questions[i],
                    answer_1=question_5_answer_1,
                    answer_2=question_5_answer_2,
                    answer_3=question_5_answer_3,
                    answer_4=question_5_answer_4,
                    day=f"{datetime.date.today()}",
                )
        users = await db.select_all_users()
        text = (
            "<b>⚡️ Loyiha doirasida yangi testlar botga qo’shildi</b>\n\n"
            "🗒 Testlarni yechish uchun pastdagi tugmani bosing"
        )
        markup_to_user = InlineKeyboardMarkup(row_width=1)

        markup_to_user.insert(InlineKeyboardButton(text="✍️ Boshlash", callback_data=f"new_test"))
        counter = 0
        bad_counter = 0
        for user in users:
            try:
                await bot.send_message(chat_id=user["telegram_id"], text=text, reply_markup=markup_to_user)
                counter += 1
                await asyncio.sleep(0.05)
            except Exception as err:
                bad_counter += 1
                await asyncio.sleep(0.05)
        await message.answer(
            f"Test yuborish yakunlandi\nTest yuborilganlar:{counter}\n" f"Yuborilmaganlar:{bad_counter}"
        )
        await state.finish()
