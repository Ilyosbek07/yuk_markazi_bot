import json

import asyncpg
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import BoundFilter, CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.config import ADMINS
from keyboards.default.all import menu, number
from keyboards.inline.all import order_button
from loader import bot, db, dp
from states.rekStates import DelUser, Number, TrackState
from utils.misc import subscription


class IsGroup(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP,
        )


class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE


@dp.message_handler(commands=["del"])
async def delete_user(message: types.Message):
    admins = await db.select_all_admins()
    admins_list = []
    for i in admins:
        admins_list.append(i[1])
    if message.from_user.id in admins_list:
        await message.answer("Id ni kiriting")
        await DelUser.user.set()


@dp.message_handler(state=DelUser.user)
async def delete(message: types.Message, state: FSMContext):
    await db.delete_users(telegram_id=int(f"{message.text}"))
    await message.answer('O"chirildi')
    await state.finish()


@dp.chat_join_request_handler()
async def new_chat_member(req: types.ChatJoinRequest):
    chanel_1 = ""
    chanel_2 = ""
    chanel_3 = ""
    chanel_4 = ""
    chanel_5 = ""
    chanel_6 = ""
    chanel_7 = ""
    chanel_8 = ""
    chanel_9 = ""
    counter = 1
    requested_link = f"{req.invite_link['invite_link']}"
    requested_user = await db.get_requested_users(telegram_id=req.from_user.id)
    channels = await db.select_req_j_chanel()

    if requested_user and channels:
        for i in channels:
            channel = i["url"]
            if counter == 1:
                chanel_1 = f"{channel[:22]}..."
            if counter == 2:
                chanel_2 = f"{channel[:22]}..."
            if counter == 3:
                chanel_3 = f"{channel[:22]}..."
            if counter == 4:
                chanel_4 = f"{channel[:22]}..."
            if counter == 5:
                chanel_5 = f"{channel[:22]}..."
            if counter == 6:
                chanel_6 = f"{channel[:22]}..."
            if counter == 7:
                chanel_7 = f"{channel[:22]}..."
            if counter == 8:
                chanel_7 = f"{channel[:22]}..."
            if counter == 9:
                chanel_9 = f"{channel[:22]}..."
            counter += 1
    if requested_link == chanel_1:
        await db.update_url_1(url_1="yes", telegram_id=req.from_user.id)
    elif requested_link == chanel_2:
        await db.update_url_2(url_2="yes", telegram_id=req.from_user.id)
    elif requested_link == chanel_3:
        await db.update_url_3(url_3="yes", telegram_id=req.from_user.id)
    elif requested_link == chanel_4:
        await db.update_url_4(url_4="yes", telegram_id=req.from_user.id)
    elif requested_link == chanel_5:
        await db.update_url_5(url_5="yes", telegram_id=req.from_user.id)
    elif requested_link == chanel_6:
        await db.update_url_6(url_6="yes", telegram_id=req.from_user.id)
    elif requested_link == chanel_7:
        await db.update_url_7(url_7="yes", telegram_id=req.from_user.id)
    elif requested_link == chanel_8:
        await db.update_url_8(url_8="yes", telegram_id=req.from_user.id)
    elif requested_link == chanel_9:
        await db.update_url_9(url_9="yes", telegram_id=req.from_user.id)

    elif not requested_user and channels:
        for i in channels:
            channel = i["url"]
            if counter == 1:
                chanel_1 = f"{channel[:22]}..."
            if counter == 2:
                chanel_2 = f"{channel[:22]}..."
            if counter == 3:
                chanel_3 = f"{channel[:22]}..."
            if counter == 4:
                chanel_4 = f"{channel[:22]}..."
            if counter == 5:
                chanel_5 = f"{channel[:22]}..."
            if counter == 6:
                chanel_6 = f"{channel[:22]}..."
            if counter == 7:
                chanel_7 = f"{channel[:22]}..."
            if counter == 8:
                chanel_8 = f"{channel[:22]}..."
            if counter == 9:
                chanel_9 = f"{channel[:22]}..."
            counter += 1

        if requested_link == chanel_1:
            await db.update_url_1(url_1="yes", telegram_id=req.from_user.id)
        elif requested_link == chanel_2:
            await db.update_url_2(url_2="yes", telegram_id=req.from_user.id)
        elif requested_link == chanel_3:
            await db.update_url_3(url_3="yes", telegram_id=req.from_user.id)
        elif requested_link == chanel_4:
            await db.update_url_4(url_4="yes", telegram_id=req.from_user.id)
        elif requested_link == chanel_5:
            await db.update_url_5(url_5="yes", telegram_id=req.from_user.id)
        elif requested_link == chanel_6:
            await db.update_url_6(url_6="yes", telegram_id=req.from_user.id)
        elif requested_link == chanel_7:
            await db.update_url_7(url_7="yes", telegram_id=req.from_user.id)
        elif requested_link == chanel_8:
            await db.update_url_8(url_8="yes", telegram_id=req.from_user.id)
        elif requested_link == chanel_9:
            await db.update_url_9(url_9="yes", telegram_id=req.from_user.id)


@dp.message_handler(IsPrivate(), CommandStart(), state="*")
async def start_bot_func(message: types.Message, state: FSMContext):
    if state:
        await state.finish()
    requested_user_is_subscribe = await db.get_requested_users(telegram_id=message.from_user.id)
    channels = await db.select_req_j_chanel()
    if requested_user_is_subscribe:
        list_chanel_id = []
        for channel in channels:
            list_chanel_id.append(channel["channel_id"])
        is_join = {
            "chanel_1": "",
            "chanel_2": "",
            "chanel_3": "",
            "chanel_4": "",
            "chanel_5": "",
            "chanel_6": "",
            "chanel_7": "",
            "chanel_8": "",
            "chanel_9": "",
        }

        join_counter = 0
        for channel in list_chanel_id:
            check_subscription = await subscription.check(user_id=message.from_user.id, channel=channel)
            join_counter += 1
            is_join[f"chanel_{join_counter}"] = check_subscription
        if is_join:
            if is_join[f"chanel_1"] == 1:
                await db.update_url_1(url_1="yes", telegram_id=message.from_user.id)
            if is_join[f"chanel_2"] == 1:
                await db.update_url_2(url_2="yes", telegram_id=message.from_user.id)
            if is_join[f"chanel_3"] == 1:
                await db.update_url_3(url_3="yes", telegram_id=message.from_user.id)
            if is_join[f"chanel_4"] == 1:
                await db.update_url_4(url_4="yes", telegram_id=message.from_user.id)
            if is_join[f"chanel_5"] == 1:
                await db.update_url_5(url_5="yes", telegram_id=message.from_user.id)
            if is_join[f"chanel_6"] == 1:
                await db.update_url_6(url_6="yes", telegram_id=message.from_user.id)
            if is_join[f"chanel_7"] == 1:
                await db.update_url_7(url_7="yes", telegram_id=message.from_user.id)
            if is_join[f"chanel_8"] == 1:
                await db.update_url_8(url_8="yes", telegram_id=message.from_user.id)
            if is_join[f"chanel_9"] == 1:
                await db.update_url_9(url_9="yes", telegram_id=message.from_user.id)

    else:
        await db.add_requested_users(telegram_id=message.from_user.id)
        list_chanel_id = []
        for channel in channels:
            list_chanel_id.append(channel["channel_id"])
        is_join = {
            "chanel_1": "",
            "chanel_2": "",
            "chanel_3": "",
            "chanel_4": "",
            "chanel_5": "",
            "chanel_6": "",
            "chanel_7": "",
            "chanel_8": "",
            "chanel_9": "",
        }

        join_counter = 0
        for channel in list_chanel_id:
            check_subscription = await subscription.check(user_id=message.from_user.id, channel=channel)
            join_counter += 1
            is_join[f"chanel_{join_counter}"] = check_subscription
        if is_join:
            if is_join[f"chanel_1"] == 1:
                await db.update_url_1(url_1="yes", telegram_id=message.from_user.id)
            if is_join[f"chanel_2"] == 1:
                await db.update_url_2(url_2="yes", telegram_id=message.from_user.id)
            if is_join[f"chanel_3"] == 1:
                await db.update_url_3(url_3="yes", telegram_id=message.from_user.id)
            if is_join[f"chanel_4"] == 1:
                await db.update_url_4(url_4="yes", telegram_id=message.from_user.id)
            if is_join[f"chanel_5"] == 1:
                await db.update_url_5(url_5="yes", telegram_id=message.from_user.id)
            if is_join[f"chanel_6"] == 1:
                await db.update_url_6(url_6="yes", telegram_id=message.from_user.id)
            if is_join[f"chanel_7"] == 1:
                await db.update_url_7(url_7="yes", telegram_id=message.from_user.id)
            if is_join[f"chanel_8"] == 1:
                await db.update_url_8(url_8="yes", telegram_id=message.from_user.id)
            if is_join[f"chanel_9"] == 1:
                await db.update_url_9(url_9="yes", telegram_id=message.from_user.id)

    if_old = await db.select_user(telegram_id=message.from_user.id)
    args = message.get_args()
    elements = await db.get_elements()
    photo = ""
    gifts = ""
    for element in elements:
        photo += f"{element['photo']}"
        gifts += f"{element['gifts']}"

    requested_user = await db.get_requested_users(telegram_id=message.from_user.id)
    button = types.InlineKeyboardMarkup(
        row_width=1,
    )
    status = True
    all = await db.select_chanel()
    add_list_channel = await db.select_add_list_channels()
    add_list = await db.select_add_list()
    chanels = []
    url = []
    channel_names = []
    for add_lst in add_list:
        url.append(add_lst["url"])
        channel_names.append(add_lst["button_name"])

    for channel in add_list_channel:
        chanels.append(channel["url"])

    for i in all:
        chanels.append(i["chanelll"])
        url.append(i["url"])
        channel_names.append(i["channel_name"])

    for channel in chanels:
        status *= await subscription.check(user_id=message.from_user.id, channel=f"{channel}")

    if requested_user:
        counter = 1
        for channel in channels:
            if requested_user[0][counter] != "yes":
                button.add(types.InlineKeyboardButton(text=channel["channel_name"], url=f"{channel['url']}"))
            counter += 1
    else:
        for channel in channels:
            button.add(types.InlineKeyboardButton(text=channel["channel_name"], url=f"{channel['url']}"))

    len_buttons = len(button["inline_keyboard"])
    if args and not if_old:
        try:
            user = await db.add_user(
                telegram_id=message.from_user.id,
                full_name=message.from_user.full_name,
                username=message.from_user.username,
                phone="---",
                oldd="new",
                user_args=f"{args}",
            )
        except asyncpg.exceptions.UniqueViolationError:
            user = await db.update_user_args(user_args=f"{args}", telegram_id=message.from_user.id)

        if status and len_buttons == 0:
            if user[3] == "---":
                result = (f"<b>Assalomu aleykum.\n\n"
                          f"Bu bot orqali siz yuklaringizni jo'natishingiz yoki buyurtma olishingiz mumkin!</b>")
                await message.answer(result, disable_web_page_preview=True)
                await message.answer(
                    '<b>"📲 Raqamni yuborish"</b> tugmasini bosgan holda raqamingizni yuboring!',
                    reply_markup=number,
                    disable_web_page_preview=True,
                )
                await Number.number.set()
            else:
                await message.answer(
                    """✍️1.Buyurtmangiz haqida ma'lumot qoldirish uchun - /buyurtma_berish!!!\n🚛2.Buyurtmalar bilan bog'lanish uchun - /buyurtma_olish!!!\n\n______________________________
✍️1.Буюртмангиз ҳақида маълумот қолдириш учун - /buyurtma_berish!!!\n🚛2.Буюртмалар билан боғланиш учун - /buyurtma_olish!!!""",
                    reply_markup=menu,
                    disable_web_page_preview=True,
                )
        else:
            counter = 0
            for i in url:
                button.add(types.InlineKeyboardButton(f"{channel_names[counter]}", url=f"https://t.me/{i}"))
                counter += 1
            button.add(types.InlineKeyboardButton(text="✅ Азо бўлдим", callback_data="check_subs"))

            await message.answer(
                """🚀 Botdan foydalanish uchun quyidagilarga kanallarga azo boʼling. Keyin <b>"✅ А'zo boʼldim"</b> tugmasini bosing\n\n<i>⚠️ Yopiq kanallarga ulanish soʼrovini yuborishingiz kifoya.</i>""",
                reply_markup=button,
                disable_web_page_preview=True,
            )

    elif not args and not if_old:
        try:
            user = await db.add_user(
                telegram_id=message.from_user.id,
                full_name=message.from_user.full_name,
                username=message.from_user.username,
                phone="---",
                oldd="not",
                user_args="not_args",
            )
        except asyncpg.exceptions.UniqueViolationError:
            user = await db.select_user(telegram_id=message.from_user.id)

        if status and len_buttons == 0:
            if user[3] == "---":
                await message.answer(
                    '<b>"📲 Raqamni yuborish"</b> tugmasini bosgan holda raqamingizni yuboring!',
                    reply_markup=number,
                    disable_web_page_preview=True,
                )
                await Number.number.set()
            else:
                await message.answer(
                    """✍️1.Buyurtmangiz haqida ma'lumot qoldirish uchun - /buyurtma_berish!!!\n🚛2.Buyurtmalar bilan bog'lanish uchun - /buyurtma_olish!!!\n\n______________________________
✍️1.Буюртмангиз ҳақида маълумот қолдириш учун - /buyurtma_berish!!!\n🚛2.Буюртмалар билан боғланиш учун - /buyurtma_olish!!!""",
                    reply_markup=menu,
                    disable_web_page_preview=True,
                )
        else:
            counter = 0
            for i in url:
                button.add(types.InlineKeyboardButton(f"{channel_names[counter]}", url=f"https://t.me/{i}"))
                counter += 1
            button.add(types.InlineKeyboardButton(text="✅ Азо бўлдим", callback_data="check_subs"))

            await message.answer(
                """🚀 Botdan foydalanish uchun quyidagilarga kanallarga azo boʼling. Keyin <b>"✅ А'zo boʼldim"</b> tugmasini bosing\n\n<i>⚠️ Yopiq kanallarga ulanish soʼrovini yuborishingiz kifoya.</i>""",
                reply_markup=button,
                disable_web_page_preview=True,
            )
    elif args and if_old[7] == "000" and int(args) != if_old[6]:
        try:
            await db.update_user_args_oldd(
                oldd="new", user_args=f"{args}", phone="---", telegram_id=message.from_user.id
            )
        except asyncpg.exceptions.UniqueViolationError:
            pass
        user = await db.select_user(telegram_id=message.from_user.id)

        if status and len_buttons == 0:
            if user[3] == "---":
                await message.answer(
                    '<b>"📲 Raqamni yuborish"</b> tugmasini bosgan holda raqamingizni yuboring!',
                    reply_markup=number,
                    disable_web_page_preview=True,
                )
                await Number.number.set()
            else:
                await message.answer(
                    """✍️1.Buyurtmangiz haqida ma'lumot qoldirish uchun - /buyurtma_berish!!!\n🚛2.Buyurtmalar bilan bog'lanish uchun - /buyurtma_olish!!!\n\n______________________________
✍️1.Буюртмангиз ҳақида маълумот қолдириш учун - /buyurtma_berish!!!\n🚛2.Буюртмалар билан боғланиш учун - /buyurtma_olish!!!""",
                    reply_markup=menu,
                    disable_web_page_preview=True,
                )
        else:
            counter = 0
            for i in url:
                button.add(types.InlineKeyboardButton(f"{channel_names[counter]}", url=f"https://t.me/{i}"))
                counter += 1
            button.add(types.InlineKeyboardButton(text="✅ Азо бўлдим", callback_data="check_subs"))

            await message.answer(
                """🚀 Botdan foydalanish uchun quyidagilarga kanallarga azo boʼling. Keyin <b>"✅ А'zo boʼldim"</b> tugmasini bosing\n\n<i>⚠️ Yopiq kanallarga ulanish soʼrovini yuborishingiz kifoya.</i>""",
                reply_markup=button,
                disable_web_page_preview=True,
            )

    else:
        try:
            user = await db.add_user(
                telegram_id=message.from_user.id,
                full_name=message.from_user.full_name,
                username=message.from_user.username,
                phone="---",
                oldd="not",
                user_args="not_args",
            )
        except asyncpg.exceptions.UniqueViolationError:
            user = await db.select_user(telegram_id=message.from_user.id)
        for channel in chanels:
            status *= await subscription.check(user_id=message.from_user.id, channel=f"{channel}")
        if status and len_buttons == 0:
            if user[3] == "---":
                await message.answer(
                    '<b>📲 Raqamni yuborish"</b> tugmasini bosgan holda raqamingizni yuboring!',
                    reply_markup=number,
                    disable_web_page_preview=True,
                )
                await Number.number.set()
            else:
                await message.answer(
                    """✍️1.Buyurtmangiz haqida ma'lumot qoldirish uchun - /buyurtma_berish!!!\n🚛2.Buyurtmalar bilan bog'lanish uchun - /buyurtma_olish!!!\n\n______________________________
✍️1.Буюртмангиз ҳақида маълумот қолдириш учун - /buyurtma_berish!!!\n🚛2.Буюртмалар билан боғланиш учун - /buyurtma_olish!!!""",
                    reply_markup=menu,
                    disable_web_page_preview=True,
                )
        else:
            counter = 0
            for i in url:
                button.add(types.InlineKeyboardButton(f"{channel_names[counter]}", url=f"https://t.me/{i}"))
                counter += 1
            button.add(types.InlineKeyboardButton(text="✅ A'zo bo'ldim", callback_data="check_subs"))

            await message.answer(
                """🚀 Botdan foydalanish uchun quyidagilarga kanallarga azo boʼling. Keyin <b>"✅ А'zo boʼldim"</b> tugmasini bosing\n\n<i>⚠️ Yopiq kanallarga ulanish soʼrovini yuborishingiz kifoya.</i>""",
                reply_markup=button,
                disable_web_page_preview=True,
            )


@dp.message_handler(state=Number.number, content_types=types.ContentType.CONTACT)
async def phone_number(message: types.Message, state: FSMContext):
    elements = await db.get_elements()
    scoree = 0
    for element in elements:
        scoree += element["limit_score"]

    user = await db.select_user(telegram_id=message.from_user.id)
    user_number = f"{message.contact.phone_number}"
    if user_number.startswith("+998") or user_number.startswith("998"):
        if user[3] == "---":
            await db.update_user_phone(
                phone=message.contact.phone_number,
                score=scoree,
                telegram_id=message.from_user.id,
            )
            await message.answer(
                """✍️1.Buyurtmangiz haqida ma'lumot qoldirish uchun - /buyurtma_berish!!!\n🚛2.Buyurtmalar bilan bog'lanish uchun - /buyurtma_olish!!!\n\n______________________________
✍️1.Буюртмангиз ҳақида маълумот қолдириш учун - /buyurtma_berish!!!\n🚛2.Буюртмалар билан боғланиш учун - /buyurtma_olish!!!"""
            )

            if user[5] == "new":
                args_user = await db.select_user(telegram_id=int(user[7]))

                update_score = int(args_user[4]) + scoree
                await db.update_user_score(score=update_score, telegram_id=int(user[7]))

                await bot.send_message(
                    chat_id=int(user[7]),
                    text=f"<b>👤 Yangi ishtirokchi qo'shildi\n"
                         f"🎗 Sizning balingiz {update_score}\n"
                         f"🔊 Ko'proq do'stlaringizni taklfi qilib ballaringizni oshiring!</b>",
                )
            await message.answer(
                "<b>Quyidagi menyudan kerakli boʼlimni tanlang 👇</b>", reply_markup=menu, disable_web_page_preview=True
            )
            await state.finish()
        else:
            await message.answer(
                "<b>Quyidagi menyudan kerakli boʼlimni tanlang 👇</b>", reply_markup=menu, disable_web_page_preview=True
            )
            await state.finish()
    else:
        await message.answer(
            "Kechirasiz Faqat O`zbekiston raqamlarini qabul qilamiz", reply_markup=types.ReplyKeyboardRemove()
        )
        await state.finish()


@dp.message_handler(text="Buyurtma berish/Буюртма бериш")
async def order_with_button(message: types.Message):
    f = open('handlers/json_data/regions.json')
    data = json.load(f)
    but = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, )
    but.add(*(KeyboardButton(text=f"{region['name']}") for region in data))
    but.add((KeyboardButton(text='🛑 Bekor qilish')))
    await message.answer("Yukingizni olish uchun mashina"
                         " borishi kerak bo'lgan hududni belgilang!!!\n\n______________________________\n"
                         "Юкингизни олиш учун машина бориши керак бўлган ҳудудни белгиланг!!!",
                         reply_markup=but)

    await TrackState.region.set()


@dp.message_handler(commands="buyurtma_berish")
async def order(message: types.Message):
    f = open('handlers/json_data/regions.json')
    data = json.load(f)
    but = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, )
    but.add(*(KeyboardButton(text=f"{region['name']}") for region in data))
    but.add((KeyboardButton(text='🛑 Bekor qilish')))
    await message.answer("Yukingizni olish uchun mashina"
                         " borishi kerak bo'lgan hududni belgilang!!!\n\n______________________________\n"
                         "Юкингизни олиш учун машина бориши керак бўлган ҳудудни белгиланг!!!",
                         reply_markup=but)

    await TrackState.region.set()


@dp.message_handler(state=TrackState.region)
async def region(message: types.Message, state: FSMContext):
    if message.text and message.text == "🛑 Bekor qilish":
        await message.answer("Bosh Menu", reply_markup=menu)
        await state.finish()
    elif message.text:
        id = 0
        if message.text == 'Andijon':
            id += 1
        elif message.text == 'Buxoro':
            id += 2
        elif message.text == 'Jizzax':
            id += 3
        elif message.text == 'Qashqadaryo':
            id += 4
        elif message.text == 'Navoiy':
            id += 5
        elif message.text == 'Namangan':
            id += 6
        elif message.text == 'Samarqand':
            id += 7
        elif message.text == 'Surxondaryo':
            id += 8
        elif message.text == 'Sirdaryo':
            id += 9
        elif message.text == 'Toshkent shahri':
            id += 10
        elif message.text == 'Toshkent':
            id += 11
        elif message.text == 'Farg`ona':
            id += 12
        elif message.text == 'Xorazm':
            id += 13
        elif message.text == 'Qoraqalpog`iston':
            id += 14
        await state.update_data(
            {
                'from_region': message.text
            }
        )

        f = open('handlers/json_data/districts.json')
        data = json.load(f)

        but = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, )
        but.add(*(KeyboardButton(text=str(region['name'])) for region in data if id == region['region_id']))
        but.add((KeyboardButton(text='🛑 Bekor qilish')))
        await message.answer(f"📍Tumaningizni tanlang 👇!!!\n\n"
                             f"-----------------------------------\n"
                             f"📍Туманингизни танланг 👇!!!", reply_markup=but)

        await TrackState.district.set()


@dp.message_handler(state=TrackState.district)
async def district(message: types.Message, state: FSMContext):
    if message.text and message.text == "🛑 Bekor qilish":
        await message.answer("Bosh Menu", reply_markup=menu)
        await state.finish()
    elif message.text:
        await state.update_data(
            {
                'from_district': message.text
            }
        )

        f = open('handlers/json_data/regions.json')
        data = json.load(f)

        but = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, )
        but.add(*(KeyboardButton(text=str(region['name'])) for region in data))
        but.add((KeyboardButton(text='🛑 Bekor qilish')))

        await message.answer("Yukingizni olib"
                             " borish kerak bo'lgan hududni belgilang!!!\n\n______________________________\n"
                             "Юкингизни олиб бориш керак бўлган ҳудудни белгиланг!!!",
                             reply_markup=but)
        await TrackState.to_region.set()


@dp.message_handler(state=TrackState.to_region)
async def to_region(message: types.Message, state: FSMContext):
    if message.text and message.text == "🛑 Bekor qilish":
        await message.answer("Bosh Menu", reply_markup=menu)
        await state.finish()
    elif message.text:
        id = 0
        if message.text == 'Andijon':
            id += 1
        elif message.text == 'Buxoro':
            id += 2
        elif message.text == 'Jizzax':
            id += 3
        elif message.text == 'Qashqadaryo':
            id += 4
        elif message.text == 'Navoiy':
            id += 5
        elif message.text == 'Namangan':
            id += 6
        elif message.text == 'Samarqand':
            id += 7
        elif message.text == 'Surxondaryo':
            id += 8
        elif message.text == 'Sirdaryo':
            id += 9
        elif message.text == 'Toshkent shahri':
            id += 10
        elif message.text == 'Toshkent':
            id += 11
        elif message.text == 'Farg`ona':
            id += 12
        elif message.text == 'Xorazm':
            id += 13
        elif message.text == 'Qoraqalpog`iston':
            id += 14
        await state.update_data(
            {
                'to_region': message.text
            }
        )

        f = open('handlers/json_data/districts.json')
        data = json.load(f)

        but = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, )
        but.add(*(KeyboardButton(text=str(region['name'])) for region in data if id == region['region_id']))
        but.add((KeyboardButton(text='🛑 Bekor qilish')))
        await message.answer(f"📍 Yuk olib borilishi kerak bo'lgan Tumanni tanlang 👇\n\n"
                             f"-----------------------------------\n"
                             f"📍 Юк олиб борилиши керак бўлган Туманни танланг 👇", reply_markup=but)
        await TrackState.to_district.set()


@dp.message_handler(state=TrackState.to_district)
async def to_district(message: types.Message, state: FSMContext):
    if message.text and message.text == "🛑 Bekor qilish":
        await message.answer("Bosh Menu", reply_markup=menu)
        await state.finish()
    elif message.text:
        but = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, )
        but.add((KeyboardButton(text='🛑 Bekor qilish')))

        await message.answer(
            "Yukingiz haqida qo'shimcha ma'lumot kiriting!!!(masalan: yuk turi, "
            "og'irligi, qancha narx taklif qilishingiz va hokazo)", reply_markup=but)

        await state.update_data(
            {
                'to_district': message.text
            }
        )
        await TrackState.data.set()


@dp.message_handler(state=TrackState.data)
async def result(message: types.Message, state: FSMContext):
    if message.text and message.text == "🛑 Bekor qilish":
        await message.answer("Bosh Menu", reply_markup=menu)
        await state.finish()
    elif message.text:
        await state.update_data({
            'description': message.text
        })
        data = await state.get_data()
        status_button = ReplyKeyboardMarkup(resize_keyboard=True)
        status_button.add(KeyboardButton(text="✅ Tasdiqlash"))
        status_button.add(KeyboardButton(text="🛑 Bekor qilish"))
        await message.answer(f"🗒 Yukingiz haqidagi ma'lumotlar:\n"
                             f"{data.get('from_region')} {data.get('from_district')}dan {data.get('to_region')} {data.get('to_district')}ga yetkazib berish kerak!!!\n\n"
                             f"Buyurtma haqida ma'lumot:\n"
                             f"{message.text}\n\n"
                             f"-------------------------------------------------------------------\n"
                             f"🗒 Юкингиз ҳақидаги маълумотлар:\n"
                             f"{data.get('from_region')} {data.get('from_district')}дан "
                             f"{data.get('to_region')} {data.get('to_district')}га етказиб бериш керак!!!\n\n"
                             f"{message.text}",
                             reply_markup=status_button)
        await TrackState.status.set()


@dp.message_handler(state=TrackState.status)
async def status(message: types.Message, state: FSMContext):
    if message.text == "✅ Tasdiqlash":
        data = await state.get_data()
        order = await db.add_order(
            from_region=data.get('from_region'),
            from_district=data.get('from_district'),
            to_region=data.get('to_region'),
            to_district=data.get('to_district'),
            description=data.get('description'),
            status=data.get('registered'),
            customer_id=message.from_user.id
        )
        group_id = await db.get_elements()
        user = await db.get_user(telegram_id=message.from_user.id)
        order_detail = (f"<b>{order['id']}# - ID\n🗒 Yangi Buyurtma keldi.\n\n"
                        f"Ma'lumotlar:\n\n{data.get('from_region')} {data.get('from_district')}dan {data.get('to_region')} {data.get('to_district')}ga yetkazib berish kerak!!!\n\n"
                        f"Buyurtma haqida ma'lumot:\n"
                        f"{data.get('description')}</b>\n\n"
                        f"Buyurtmachining ma'lumotlari:\n\n"
                        f"👤 Ismi: {user[0][1]}\n"
                        f"📞 Raqami: {user[0][3]}\n"
                        f"Username: @{user[0][2]}\n\n")
        await bot.send_message(chat_id=group_id[0][-1], text=order_detail, reply_markup=order_button)
        await message.answer("Buyurtmangiz qabul qilindi!!!\n\n"
                             "Adminlar siz bilan tez orada bog'lanishadi!!!", reply_markup=menu)
        await state.finish()
    elif message.text == "🛑 Bekor qilish":
        await message.answer("Buyurtmangiz bekor qilindi!!!", reply_markup=menu)
        await state.finish()
    else:
        await message.answer("Iltimos, quyidagi tugmalardan birini bosing!!! 👇")


@dp.message_handler(text="Buyurtma olish / Буюртма олиш")
async def get_order_with_button(message: types.Message):
    f = open('handlers/json_data/regions.json')
    data = json.load(f)
    but = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, )
    but.add(*(KeyboardButton(text=f"{region['name']}") for region in data))
    but.add((KeyboardButton(text='🛑 Bekor qilish')))

    await message.answer("🗺 Qaysi hududan yuk kerak ekanligini belgilang!!!"
                         "\n\n_______________________\n"
                         "🗺Қайси ҳудудан юк керак эканлигини белгиланг!!!",
                         reply_markup=but)
    await TrackState.get_order.set()


@dp.message_handler(commands="buyurtma_olish")
async def get_order(message: types.Message):
    f = open('handlers/json_data/regions.json')
    data = json.load(f)
    but = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, )
    but.add(*(KeyboardButton(text=f"{region['name']}") for region in data))
    but.add((KeyboardButton(text='🛑 Bekor qilish')))

    await message.answer("🗺 Qaysi hududan yuk kerak ekanligini belgilang!!!"
                         "\n\n_______________________\n"
                         "🗺Қайси ҳудудан юк керак эканлигини белгиланг!!!",
                         reply_markup=but)
    await TrackState.get_order.set()


@dp.message_handler(state=TrackState.get_order)
async def get_order_group(message: types.Message, state: FSMContext):
    if message.text == "🛑 Bekor qilish":
        await message.answer("Bosh Menu", reply_markup=menu)
    elif message.text != "🛑 Bekor qilish":
        await message.answer("O'zingizga mos buyurtma bilan bog'lanish uchun adminga yozin!!!\n\n"
                             "______________________________\n"
                             "Ўзингизга мос буюртма билан боғланиш учун админга ёзинг!!!\n", reply_markup=menu)
        await state.finish()


@dp.callback_query_handler(text="filling_property")
async def filling_property_answer(call: types.CallbackQuery):
    await call.message.delete()
    elements = await db.get_elements()
    bot_username = (await bot.get_me()).username

    await call.message.answer(f"{elements[0][2]}"
                              f"\n\nhttps://t.me/{bot_username}?start={call.from_user.id}")


@dp.callback_query_handler(text="earn_money")
async def earn_money_answer(call: types.CallbackQuery):
    await call.message.delete()
    elements = await db.get_elements()
    bot_username = (await bot.get_me()).username

    await call.message.answer(f"{elements[0][3]}"
                              f"\n\nhttps://t.me/{bot_username}?start={call.from_user.id}")


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    requested_user_is_subscribe = await db.get_requested_users(telegram_id=call.from_user.id)
    channels = await db.select_req_j_chanel()
    if requested_user_is_subscribe:
        list_chanel_id = []
        for channel in channels:
            list_chanel_id.append(channel["channel_id"])
        is_join = {
            "chanel_1": "",
            "chanel_2": "",
            "chanel_3": "",
            "chanel_4": "",
            "chanel_5": "",
            "chanel_6": "",
            "chanel_7": "",
            "chanel_8": "",
            "chanel_9": "",
        }

        join_counter = 0
        for channel in list_chanel_id:
            check_subscription = await subscription.check(user_id=call.from_user.id, channel=channel)
            join_counter += 1
            is_join[f"chanel_{join_counter}"] = check_subscription
        if is_join[f"chanel_1"] == 1:
            await db.update_url_1(url_1="yes", telegram_id=call.from_user.id)
        if is_join[f"chanel_2"] == 1:
            await db.update_url_2(url_2="yes", telegram_id=call.from_user.id)
        if is_join[f"chanel_3"] == 1:
            await db.update_url_3(url_3="yes", telegram_id=call.from_user.id)
        if is_join[f"chanel_4"] == 1:
            await db.update_url_4(url_4="yes", telegram_id=call.from_user.id)
        if is_join[f"chanel_5"] == 1:
            await db.update_url_5(url_5="yes", telegram_id=call.from_user.id)
        if is_join[f"chanel_6"] == 1:
            await db.update_url_6(url_6="yes", telegram_id=call.from_user.id)
        if is_join[f"chanel_7"] == 1:
            await db.update_url_7(url_7="yes", telegram_id=call.from_user.id)
        if is_join[f"chanel_8"] == 1:
            await db.update_url_8(url_8="yes", telegram_id=call.from_user.id)
        if is_join[f"chanel_9"] == 1:
            await db.update_url_9(url_9="yes", telegram_id=call.from_user.id)

    else:
        await db.add_requested_users(telegram_id=call.from_user.id)
        list_chanel_id = []
        for channel in channels:
            list_chanel_id.append(channel["channel_id"])
        is_join = {
            "chanel_1": "",
            "chanel_2": "",
            "chanel_3": "",
            "chanel_4": "",
            "chanel_5": "",
            "chanel_6": "",
            "chanel_7": "",
            "chanel_8": "",
            "chanel_9": "",
        }

        join_counter = 0
        for channel in list_chanel_id:
            check_subscription = await subscription.check(user_id=call.from_user.id, channel=channel)
            join_counter += 1
            is_join[f"chanel_{join_counter}"] = check_subscription
        if is_join[f"chanel_1"] == 1:
            await db.update_url_1(url_1="yes", telegram_id=call.from_user.id)
        if is_join[f"chanel_2"] == 1:
            await db.update_url_2(url_2="yes", telegram_id=call.from_user.id)
        if is_join[f"chanel_3"] == 1:
            await db.update_url_3(url_3="yes", telegram_id=call.from_user.id)
        if is_join[f"chanel_4"] == 1:
            await db.update_url_4(url_4="yes", telegram_id=call.from_user.id)
        if is_join[f"chanel_5"] == 1:
            await db.update_url_5(url_5="yes", telegram_id=call.from_user.id)
        if is_join[f"chanel_6"] == 1:
            await db.update_url_6(url_6="yes", telegram_id=call.from_user.id)
        if is_join[f"chanel_7"] == 1:
            await db.update_url_7(url_7="yes", telegram_id=call.from_user.id)
        if is_join[f"chanel_8"] == 1:
            await db.update_url_8(url_8="yes", telegram_id=call.from_user.id)
        if is_join[f"chanel_9"] == 1:
            await db.update_url_9(url_9="yes", telegram_id=call.from_user.id)

    await call.answer()
    status = True
    all = await db.select_chanel()
    add_list_channel = await db.select_add_list_channels()
    add_list = await db.select_add_list()
    chanels = []
    url = []
    channel_names = []
    for add_lst in add_list:
        url.append(add_lst["url"])
        channel_names.append(add_lst["button_name"])
    for channel in add_list_channel:
        chanels.append(channel["url"])

    for i in all:
        chanels.append(i["chanelll"])
        url.append(i["url"])
        channel_names.append(i["channel_name"])
    requested_user = await db.get_requested_users(telegram_id=call.from_user.id)
    button = types.InlineKeyboardMarkup(
        row_width=1,
    )

    if requested_user:
        counter = 1
        for channel in channels:
            if requested_user[0][counter] != "yes":
                button.add(types.InlineKeyboardButton(text=channel["channel_name"], url=f"{channel['url']}"))
            counter += 1
    else:
        for channel in channels:
            button.add(types.InlineKeyboardButton(text=channel["channel_name"], url=f"{channel['url']}"))

    len_buttons = len(button["inline_keyboard"])
    result = str()
    elements = await db.get_elements()
    photo = ""
    gifts = ""
    for element in elements:
        photo += f"{element['photo']}"
        gifts += f"{element['gifts']}"

    for channel in chanels:
        status *= await subscription.check(user_id=call.from_user.id, channel=f"{channel}")
    if status and len_buttons == 0:
        user = await db.select_user(telegram_id=call.from_user.id)
        if user[3] == "---":
            result += f"<b>Tabriklaymiz, siz muvaffaqiyatli roʼyxatdan oʼtdingiz ✅</b>"
            await call.message.answer(result, disable_web_page_preview=True)
            await call.message.answer_photo(photo, caption=f"{gifts}")
            await call.message.answer(
                '<b>"📲 Raqamni yuborish"</b> tugmasini bosgan holda raqamingizni yuboring!',
                reply_markup=number,
                disable_web_page_preview=True,
            )
            await Number.number.set()
        else:
            await call.message.answer(
                """✍️1.Buyurtmangiz haqida ma'lumot qoldirish uchun - /buyurtma_berish!!!\n🚛2.Buyurtmalar bilan bog'lanish uchun - /buyurtma_olish!!!\n\n______________________________
✍️1.Буюртмангиз ҳақида маълумот қолдириш учун - /buyurtma_berish!!!\n🚛2.Буюртмалар билан боғланиш учун - /buyurtma_olish!!!""",
                reply_markup=menu,
                disable_web_page_preview=True,
            )

    else:
        counter = 0
        for i in url:
            button.add(types.InlineKeyboardButton(f"{channel_names[counter]}", url=f"https://t.me/{i}"))
            counter += 1
        button.add(types.InlineKeyboardButton(text="✅ А'zo boʼldim", callback_data="check_subs"))

        await call.message.answer(
            """🚀 Botdan foydalanish uchun quyidagilarga kanallarga azo boʼling. Keyin <b>"✅ А'zo boʼldim"</b> tugmasini bosing\n\n<i>⚠️ Yopiq kanallarga ulanish soʼrovini yuborishingiz kifoya.</i>""",
            reply_markup=button,
            disable_web_page_preview=True,
        )
