from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Buyurtma berish/Буюртма бериш"),
        ],
        [
            KeyboardButton(text="Buyurtma olish / Буюртма олиш"),
        ],
        [
            KeyboardButton(text="Malumotlarim / Малумотларим"),
        ],
        [
            KeyboardButton(text="Bot haqida / Бот ҳақида"),
        ],
    ],
    resize_keyboard=True,
)

number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📲 Raqamni yuborish", request_contact=True),
        ],
    ],
    resize_keyboard=True,
)
