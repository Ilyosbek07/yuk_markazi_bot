import json
import asyncpg
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import BoundFilter, CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.all import menu, number
from loader import bot, db, dp
from states.rekStates import TrackState


@dp.message_handler(commands="buyurtma_berish")
async def order(message: types.Message):
    f = open('json_data/regions.json')
    data = json.load(f)

    but = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, )
    but.add(*(KeyboardButton(text=str(region['name'])) for region in data))
    but.add(*(KeyboardButton(text='🛑 Bekor qilish')))
    await message.answer("🛍 Yukingizni olish uchun mashina"
                         " borishi kerak bo'lgan hududni belgilang!!!\n\n______________________________\n"
                         "🛍 Юкингизни олиш учун машина бориши керак бўлган ҳудудни белгиланг!!!",
                         reply_markup=but)

    await TrackState.region.set()


@dp.message_handler(state=TrackState.region)
async def region(message: types.Message, state: FSMContext):
    if message.text:
        id = 0
        if message.text == 'Andijon viloyati':
            id += 1
        elif message.text == 'Buxoro viloyati':
            id += 2
        elif message.text == 'Jizzax viloyati':
            id += 3
        elif message.text == 'Qashqadaryo viloyati':
            id += 4
        elif message.text == 'Navoiy viloyati':
            id += 5
        elif message.text == 'Namangan viloyati':
            id += 6
        elif message.text == 'Samarqand viloyati':
            id += 7
        elif message.text == 'Surxondaryo viloyati':
            id += 8
        elif message.text == 'Sirdaryo viloyati':
            id += 9
        elif message.text == 'Toshkent shahri':
            id += 10
        elif message.text == 'Toshkent viloyati':
            id += 11
        elif message.text == 'Farg`ona viloyati':
            id += 12
        elif message.text == 'Xorazm viloyati':
            id += 13
        elif message.text == 'Qoraqalpog`iston':
            id += 14
        await state.update_data(
            {
                'from_region': message.text
            }
        )

        f = open('json_data/districts.json')
        data = json.load(f)

        but = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, )
        but.add(*(KeyboardButton(text=str(region['name'])) for region in data if id == region['region_id']))
        but.add(*(KeyboardButton(text='🛑 Bekor qilish')))
        await message.answer(f"📍Tumaningizni tanlang 👇!!!\n\n"
                             f"-----------------------------------\n"
                             f"📍Туманингизни танланг 👇!!!", reply_markup=but)

        await TrackState.district.set()

@dp.message_handler(state=TrackState.district)
async def district(message: types.Message, state: FSMContext):
    if message.text:
        await state.update_data(
            {
                'from_district': message.text
            }
        )


        f = open('json_data/regions.json')
        data = json.load(f)

        but = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, )
        but.add(*(KeyboardButton(text=str(region['name'])) for region in data))
        but.add(*(KeyboardButton(text='🛑 Bekor qilish')))

        await message.answer("🛍 Yukingizni olib"
                             " borish kerak bo'lgan hududni belgilang!!!\n\n______________________________\n"
                             "🛍 Юкингизни олиб бориш керак бўлган ҳудудни белгиланг!!!",
                             reply_markup=but)
        await TrackState.to_region.set()


@dp.message_handler(state=TrackState.to_region)
async def to_region(message: types.Message, state:FSMContext):
    if message.text:
        id = 0
        if message.text == 'Andijon viloyati':
            id += 1
        elif message.text == 'Buxoro viloyati':
            id += 2
        elif message.text == 'Jizzax viloyati':
            id += 3
        elif message.text == 'Qashqadaryo viloyati':
            id += 4
        elif message.text == 'Navoiy viloyati':
            id += 5
        elif message.text == 'Namangan viloyati':
            id += 6
        elif message.text == 'Samarqand viloyati':
            id += 7
        elif message.text == 'Surxondaryo viloyati':
            id += 8
        elif message.text == 'Sirdaryo viloyati':
            id += 9
        elif message.text == 'Toshkent shahri':
            id += 10
        elif message.text == 'Toshkent viloyati':
            id += 11
        elif message.text == 'Farg`ona viloyati':
            id += 12
        elif message.text == 'Xorazm viloyati':
            id += 13
        elif message.text == 'Qoraqalpog`iston':
            id += 14
        await state.update_data(
            {
                'to_region': message.text
            }
        )

        f = open('json_data/districts.json')
        data = json.load(f)

        but = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, )
        but.add(*(KeyboardButton(text=str(region['name'])) for region in data if id == region['region_id']))
        but.add(*(KeyboardButton(text='🛑 Bekor qilish')))
        await message.answer(f"📍Tumaningizni tanlang 👇!!!\n\n"
                             f"-----------------------------------\n"
                             f"📍Туманингизни танланг 👇!!!", reply_markup=but)

        await TrackState.to_district.set()

@dp.message_handler(state=TrackState.to_district)
async def to_district(message: types.Message, state:FSMContext):
    data = await state.get_data()
    from_region = data.get('from_region')
    await message.answer(f"Tabriklaymiz sizning ma'lumotlaringiz\n\n"
                         f"from_region")

@dp.message_handler(commands="buyurtma_olish")
async def get_order(message: types.Message):
    await message.answer("🗺 Qaysi hududan yuk kerak ekanligini belgilang!!!"
                         "\n\n_______________________\n"
                         "🗺Қайси ҳудудан юк керак эканлигини белгиланг!!!",
                         reply_markup=menu)
