from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

rekKey1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Rasm"), KeyboardButton(text="Video")],
        [KeyboardButton(text="Text"), KeyboardButton(text="Back")],
    ],
    resize_keyboard=True,
)
back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔙️ Orqaga"),
        ]
    ],
    resize_keyboard=True,
)

admin_key_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Add List ➕"),
            KeyboardButton(text="Add List ➖"),
        ],
        [
            KeyboardButton(text="Add List 📈"),
        ],
        [
            KeyboardButton(text="Add List Kanal ➕"),
            KeyboardButton(text="Add List Kanal ➖"),
        ],
        [
            KeyboardButton(text="Add List Kanallar 📈"),
        ],
    ]
)

admin_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Xabar Yuborish 🗒 "),
            # KeyboardButton(text="Test qo'shish")
        ],
        [KeyboardButton(text="Barcha Adminlar"), KeyboardButton(text="Admin ➕"), KeyboardButton(text="Admin ➖")],
        [KeyboardButton(text="Kanal ➕"), KeyboardButton(text="Kanal ➖")],
        [KeyboardButton(text="Kanallar 📈"), KeyboardButton(text="Statistika 📊")],
        [
            KeyboardButton(text="Buyurtma Tushadigan Guruh ID raqami 📄"),
        ],
        [
            KeyboardButton(text="Bot haqida ma'lumot yozish 📄"),
        ],
        [
            KeyboardButton(text="Pul Ishlash Tugmasiga javob yozish"),
        ],
        [
            KeyboardButton(text="Hisobni to'ldigadiganlarga javob yozish"),
        ],
        # [KeyboardButton(text="Taklif miqdorini kiritish 🎁"), KeyboardButton(text="O'yin haqida matn 🎮")],
        # [KeyboardButton(text="Hisobni 0 ga tushirish"), KeyboardButton(text='Shartlarni qo"shish 🖼')],
        # [KeyboardButton(text="G'oliblar sonini kirting"), KeyboardButton(text="G'oliblar haqida ma'lumot")],
        [KeyboardButton(text="Excel File"), KeyboardButton(text="🏘 Bosh menu")],
    ],
    resize_keyboard=True,
)
admin_secret_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yopiq Kanallar ro'yxati 😱"),
        ],
        [KeyboardButton(text="Yopiq Kanal ➕"), KeyboardButton(text="Yopiq Kanal ➖")],
        [KeyboardButton(text="🏘 Bosh menu")],
    ],
    resize_keyboard=True,
)
