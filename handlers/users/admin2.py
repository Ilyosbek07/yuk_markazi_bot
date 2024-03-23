from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.default.all import menu
from keyboards.default.rekKeyboards import admin_key, admin_secret_button, back
from loader import db, dp
from states.rekStates import AllState, RekData


@dp.message_handler(text="Yangi konkurs")
async def new_konkurs(message: types.Message):
    print("ishladi")
    admins = await db.select_all_admins()
    admins_list = []
    for i in admins:
        admins_list.append(i[1])
    if message.from_user.id in admins_list:
        await db.update_all_users_args(args="000")
        await message.answer("Yangi konkurs boshlandi")


@dp.message_handler(commands=["admin"])
async def admin(message: types.Message):
    admins = await db.select_all_admins()
    admins_list = []
    for i in admins:
        admins_list.append(i[1])
    if message.from_user.id in admins_list:
        await message.answer(text="Admin panel", reply_markup=admin_key)


@dp.message_handler(text="Kanal ➕")
async def add_channel(message: types.Message):
    admins = await db.select_all_admins()
    admins_list = []
    for i in admins:
        admins_list.append(i[1])
    if message.from_user.id in admins_list:
        await message.answer(
            text="Kanalni kiriting\n\n"
                 'Masalan : "@Chanel zayavkada bo`lsa &&& belgi bilan ajratib:'
                 ' chanel_id(-123123213)&&&+chanel_url&&&Kanal nomi"\n\n'
                 "-1001798189867&&&+52bZMKjCR1jY2Qy&&&asdasd - Ko`rinishida",
            reply_markup=back,
        )
        await RekData.add.set()


@dp.message_handler(state=RekData.add)
async def add_username(message: types.Message, state: FSMContext):
    text = message.text
    if text[0] == "@":
        text_split = text.split(",")

        await db.add_chanell(chanelll=f"{text_split[0]}", channel_name=f"{text_split[1]}", url=f"{text_split[0][1:]}")
        await message.answer("Qo'shildi", reply_markup=admin_key)
        await state.finish()
    elif text == "🔙️ Orqaga":
        await message.answer("Admin panel", reply_markup=admin_key)
        await state.finish()
    elif text[0] == "-":
        split_chanel = message.text.split(",")
        chanel_lst = []
        url_lst = []
        channel_name_lst = []
        for i in split_chanel:
            lst = i.split("&&&")
            chanel_lst.append(lst[0])
            url_lst.append(lst[1])
            channel_name_lst.append(lst[2])
        chanel = f"{chanel_lst}"
        url = f"{url_lst}"
        channel_name = f"{channel_name_lst}"
        ch_text = chanel.replace("'", "")
        ch_text2 = ch_text.replace(" ", "")
        u_text = url.replace("'", "")
        u_text2 = u_text.replace(" ", "")
        channel_name_text = channel_name.replace("'", "")
        channel_name_text2 = channel_name_text.replace(" ", "")

        await db.add_chanell(chanelll=ch_text2[1:-1], url=u_text2[1:-1], channel_name=channel_name_text2[1:-1])
        await message.answer("Qo'shildi", reply_markup=admin_key)
        await state.finish()

    else:
        await message.answer(
            "Xato\n\n" "@ belgi bilan yoki kanal id(-11001835334270andLink) sini link bilan birga kiriting kiriting"
        )


@dp.message_handler(text="Kanal ➖")
async def add_channel(message: types.Message):
    admins = await db.select_all_admins()
    admins_list = []
    for i in admins:
        admins_list.append(i[1])
    if message.from_user.id in admins_list:
        await message.answer(
            text="Kanalni kiriting @ belgi bilan\n\n"
                 'Masalan : "Kanal zayavkada bo`lsa chanel_id(-123123213),chanel_url"\n\n',
            reply_markup=back,
        )
        await RekData.delete.set()


@dp.message_handler(state=RekData.delete)
async def del_username(message: types.Message, state: FSMContext):
    txt = message.text
    if txt[0] == "-":
        chanel = await db.get_chanel(channel=txt)
        if not chanel:
            await message.answer("Kanal topilmadi\n" "Qaytadan urinib ko'ring")

        else:
            await db.delete_channel(chanel=txt)
            await message.answer('Kanal o"chirildi', reply_markup=admin_key)
            await state.finish()

        # await message.answer("O'chirildi")
        # await state.finish()
    elif txt[0] == "@":
        chanel = await db.get_chanel(channel=f"{txt}")
        if not chanel:
            await message.answer("Kanal topilmadi\n" "Qaytadan urinib ko'ring")

        else:
            await db.delete_channel(chanel=txt)
            await message.answer('Kanal o"chirildi', reply_markup=admin_key)
            await state.finish()
    elif txt == "🔙️ Orqaga":
        await message.answer("Admin panel", reply_markup=admin_key)
        await state.finish()


@dp.message_handler(text="Statistika 📊")
async def show_users(message: types.Message):
    a = await db.count_users()
    await message.answer(f"<b>🔷 Jami obunachilar: {a} та</b>")


@dp.message_handler(text="🏘 Bosh menu")
async def menuu(message: types.Message):
    await message.answer("Bosh menu", reply_markup=menu)


@dp.message_handler(text="Kanallar 📈")
async def channels(message: types.Message):
    channels = await db.select_chanel()
    text = ""
    for channel in channels:
        text += f"{channel['chanelll']}\n"
    try:
        await message.answer(f"{text}", reply_markup=admin_key)
    except:
        await message.answer(f"Kanallar mavjud emas")


@dp.message_handler(text="Hisobni 0 ga tushirish")
async def channels(message: types.Message):
    admins = await db.select_all_admins()
    admins_list = []
    for i in admins:
        admins_list.append(i[1])
    if message.from_user.id in admins_list:
        await message.answer("Aniqmi\n\n" "yes or no", reply_markup=types.ReplyKeyboardMarkup())
        await RekData.score_0.set()


@dp.message_handler(state=RekData.score_0)
async def channels(message: types.Message, state: FSMContext):
    if message.text == "yes":
        try:
            await db.update_users_all_score()
            await message.answer(f"Hisoblar 0 ga tushirildi", reply_markup=admin_key)
        except Exception as err:
            await message.answer(f"Muammo yuzaga keldi\n\n{err}")
    else:
        await state.finish()
        await message.answer("Bosh menu", reply_markup=admin_key)


@dp.message_handler(text="Rasmni almashtirish 🖼")
async def change_picture(message: types.Message):
    admins = await db.select_all_admins()
    admins_list = []
    for i in admins:
        admins_list.append(i[1])
    if message.from_user.id in admins_list:
        await message.answer("Rasmni kiriting", reply_markup=back)
        await RekData.picture.set()


@dp.message_handler(content_types=["photo", "text", "video"], state=RekData.picture)
async def change_picture_(message: types.Message, state: FSMContext):
    if message.photo:
        photo = message.photo[-1].file_id
        elements = await db.get_elements()
        if elements:
            await db.update_photo(photo=photo)
            await message.answer("Yangilandi", reply_markup=admin_key)
            await state.finish()

        else:
            await db.add_photo(photo=photo)
            await message.answer("Qo`shildi", reply_markup=admin_key)
            await state.finish()

    elif message.text == "🔙️ Orqaga":
        await message.answer("Bosh menu", reply_markup=menu)
        await state.finish()
    elif message.text == "/start":
        await message.answer("Bosh menu", reply_markup=menu)
        await state.finish()

    else:
        await message.answer("Faqat rasm qabul qilamiz")


@dp.message_handler(text="Pul Ishlash Tugmasiga javob yozish")
async def change_picture(message: types.Message):
    admins = await db.select_all_admins()
    admins_list = []
    for i in admins:
        admins_list.append(i[1])
    if message.from_user.id in admins_list:

        admins = await db.select_all_admins()
        admins_list = []
        for i in admins:
            admins_list.append(i[1])
        if message.from_user.id in admins_list:
            await message.answer("Textni kiriting", reply_markup=back)
            await RekData.text.set()


@dp.message_handler(state=RekData.text)
async def change_picture_(message: types.Message, state: FSMContext):
    if message.text:
        elements = await db.get_elements()
        if elements:
            await db.update_game_text(game_text=message.text)
            await message.answer("Yangilandi", reply_markup=admin_key)
            await state.finish()
        elif message.text == "/start":
            await message.answer("Bosh menu", reply_markup=menu)
            await state.finish()

        elif message.text == "🔙️ Orqaga":
            await message.answer("Bosh menu", reply_markup=menu)
            await state.finish()

        else:
            await db.add_text(game_text=message.text)
            await message.answer("Qo`shildi", reply_markup=admin_key)
            await state.finish()
    else:
        await message.answer("Faqat Text qabul qilamiz")


@dp.message_handler(text="Hisobni to'ldigadiganlarga javob yozish")
async def change_picture(message: types.Message):
    await message.answer("Habarni kiriting", reply_markup=back)
    await RekData.gift.set()


@dp.message_handler(state=RekData.gift)
async def change_picture_(message: types.Message, state: FSMContext):
    if message.text:
        elements = await db.get_elements()
        if elements:
            await db.update_gift(gift=message.text)
            await message.answer("Yangilandi", reply_markup=admin_key)
            await state.finish()
        elif message.text == "/start":
            await message.answer("Bosh menu", reply_markup=menu)
            await state.finish()

        else:
            await db.add_gift(gift=message.text)
            await message.answer("Qo`shildi", reply_markup=admin_key)
            await state.finish()

    elif message.text == "🔙️ Orqaga":
        await message.answer("Bosh menu", reply_markup=menu)
        await state.finish()
    else:
        await message.answer("Faqat Text qabul qilamiz")


@dp.message_handler(text="Taklif miqdorini kiritish 🎁")
async def change_picture(message: types.Message):
    admins = await db.select_all_admins()
    admins_list = []
    for i in admins:
        admins_list.append(i[1])
    if message.from_user.id in admins_list:
        await message.answer("Faqat son kiriting", reply_markup=back)
        await RekData.score.set()


@dp.message_handler(state=RekData.score)
async def change_picture_(message: types.Message, state: FSMContext):
    try:
        text = int(message.text)

        if text:
            elements = await db.get_elements()
            if elements:
                await db.update_limit_score(limit_score=text)
                await message.answer("Yangilandi", reply_markup=admin_key)
                await state.finish()
            # else:
            # await db.add_text()
        elif message.text == "/start":
            await message.answer("Bosh menu", reply_markup=menu)
            await state.finish()

        elif message.text == "🔙️ Orqaga":
            await message.answer("Bosh menu", reply_markup=menu)
            await state.finish()
    except:
        if message.text == "/start":
            await message.answer("Bosh menu", reply_markup=menu)
            await state.finish()

        if message.text == "🔙️ Orqaga":
            await message.answer("Bosh menu", reply_markup=menu)
            await state.finish()
        else:
            await message.answer("Faqat Son qabul qilamiz")


@dp.message_handler(text="Bot haqida ma'lumot yozish 📄")
async def about(message: types.Message):
    admins = await db.select_all_admins()
    admins_list = []
    for i in admins:
        admins_list.append(i[1])
    if message.from_user.id in admins_list:
        await message.answer("Bot haqida ma'lumotni kiriting", reply_markup=back)
        await RekData.kbsh.set()


@dp.message_handler(state=RekData.kbsh)
async def shartlarr(message: types.Message, state: FSMContext):
    if message.text:
        elements = await db.get_elements()
        if message.text == "/start":
            await message.answer("Bosh menu", reply_markup=menu)
            await state.finish()

        if elements:
            await db.update_shartlar(shartlar=message.text)
            await message.answer("Yangilandi", reply_markup=admin_key)
            await state.finish()

        else:
            await db.add_shartlar(shartlar=message.text)
            await message.answer("Qo`shildi", reply_markup=admin_key)
            await state.finish()

    elif message.text == "🔙️ Orqaga":
        await message.answer("Bosh menu", reply_markup=menu)
        await state.finish()
    else:
        await message.answer("Faqat text qabul qilamiz")


@dp.message_handler(text="Buyurtma Tushadigan Guruh ID raqami 📄")
async def add_group_id(message: types.Message):
    admins = await db.select_all_admins()
    admins_list = []
    for i in admins:
        admins_list.append(i[1])
    if message.from_user.id in admins_list:
        await message.answer("Buyurtma Tushadigan Guruh ID raqamini kiriting", reply_markup=back)
        await RekData.group_id.set()


@dp.message_handler(state=RekData.group_id)
async def add_group_id_to_db(message: types.Message, state: FSMContext):
    if message.text.startswith('-'):
        if message.text == "🔙️ Orqaga":
            await message.answer("Bosh menu", reply_markup=menu)
            await state.finish()

        elements = await db.get_elements()
        if message.text == "/start":
            await message.answer("Bosh menu", reply_markup=menu)
            await state.finish()

        if elements:
            await db.update_group_id(group_id=message.text)
            await message.answer("Yangilandi", reply_markup=admin_key)
            await state.finish()

        else:
            await db.add_group_id(group_id=message.text)
            await message.answer("Qo`shildi", reply_markup=admin_key)
            await state.finish()

    else:
        await message.answer('Xato formatda kiritdingiz\n\n'
                             'Yopiq guruh ID sini -10031231123 formatda kiriting')


@dp.message_handler(text="G'oliblar sonini kirting")
async def change_picture(message: types.Message):
    admins = await db.select_all_admins()
    admins_list = []
    for i in admins:
        admins_list.append(i[1])
    if message.from_user.id in admins_list:
        await message.answer("Faqat son kiriting", reply_markup=back)
        await RekData.winners.set()


@dp.message_handler(state=RekData.winners)
async def change_picture_(message: types.Message, state: FSMContext):
    try:
        text = int(message.text)
        if message.text == "/start":
            await message.answer("Bosh menu", reply_markup=menu)
            await state.finish()

        if text:
            elements = await db.get_elements()
            if elements:
                await db.winners(winners=text)
                await message.answer("Yangilandi", reply_markup=admin_key)
                await state.finish()

        elif message.text == "🔙️ Orqaga":
            await message.answer("Bosh menu", reply_markup=menu)
            await state.finish()
    except Exception as err:

        if message.text == "🔙️ Orqaga":
            await message.answer("Bosh menu", reply_markup=menu)
            await state.finish()
        elif message.text == "/start":
            await message.answer("Bosh menu", reply_markup=menu)
            await state.finish()

        else:
            await message.answer("Faqat Son qabul qilamiz")


@dp.message_handler(text="Barcha Adminlar")
async def add_channel(message: types.Message):
    admins = await db.select_all_admins()
    admins_list = []
    for i in admins:
        admins_list.append(i[1])
    await message.answer(f"Adminlar - {admins_list}", reply_markup=admin_key)


@dp.message_handler(text="Admin ➕")
async def add_channel(message: types.Message):
    admins = await db.select_all_admins()
    admins_list = []
    for i in admins:
        admins_list.append(i[1])
    if message.from_user.id in admins_list:
        await message.answer("Id ni kiriting", reply_markup=back)
        await AllState.env.set()


@dp.message_handler(state=AllState.env)
async def env_change(message: types.Message, state: FSMContext):
    if message.text == "🔙️ Orqaga":
        await message.answer("Admin panel", reply_markup=admin_key)
        await state.finish()
    else:
        try:
            int(message.text)
        except ValueError:
            await message.answer("Faqat son qabul qilinadi\n\n" "Qaytadan kiriting")
        admins = await db.select_all_admins()
        admins_list = []
        for i in admins:
            admins_list.append(i[1])
        if int(message.text) in admins_list:
            await message.answer("Bunday admin mavjud")
            # await AllState.env.set()
        else:
            await db.add_admin(telegram_id=int(message.text))

            await message.answer(f"Qo'shildi\n\n", reply_markup=admin_key)
            await state.finish()


@dp.message_handler(text="Admin ➖")
async def add_channel(message: types.Message):
    admins = await db.select_all_admins()
    admins_list = []
    for i in admins:
        admins_list.append(i[1])
    if message.from_user.id in admins_list:
        await message.answer("Id ni kiriting", reply_markup=back)
        await AllState.env_remove.set()


@dp.message_handler(state=AllState.env_remove)
async def env_change(message: types.Message, state: FSMContext):
    if message.text == "🔙️ Orqaga":
        await message.answer("Admin panel", reply_markup=admin_key)
        await state.finish()
    else:
        try:
            admins = await db.select_all_admins()
            admins_list = []
            for i in admins:
                admins_list.append(i[1])
            if int(message.text) in admins_list:
                await db.delete_admins(telegram_id=int(message.text))
                admins2 = await db.select_all_admins()
                admins_list2 = []
                for i in admins2:
                    admins_list2.append(i[1])

                await message.answer(f'O"chirildi\n\n' f"Hozirgi adminlar {admins_list2}", reply_markup=admin_key)
                await state.finish()
            else:
                await message.answer("Bunday admin mavjud emas\n\n" "Faqat admin id sini qabul qilamiz")
        except Exception as err:
            await message.answer(f"{err}")
            await message.answer("Faqat son qabul qilinadi\n\n" "Qaytadan kiriting")
