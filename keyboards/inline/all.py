from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

private_button = InlineKeyboardMarkup(
    inline_keyboard=[
        # [InlineKeyboardButton(text="Nomer qo'shish / Номер қўшиш", callback_data="add_number")],
        [InlineKeyboardButton(text="Pul ishlash / Пул ишлаш ", callback_data="earn_money")],
        [InlineKeyboardButton(text="Hisobni to'ldirish / Ҳисобни тўлдириш", callback_data="filling_property")],
    ]
)
order_button = InlineKeyboardMarkup(
    inline_keyboard=[
        # [InlineKeyboardButton(text="Nomer qo'shish / Номер қўшиш", callback_data="add_number")],
        [
            InlineKeyboardButton(text="Tasdiqlash ✅", callback_data="confirm"),
            InlineKeyboardButton(text="Bekor qilish 🛑", callback_data="cancel")
        ],
        # [InlineKeyboardButton(text="Kuryer qo'shish", callback_data="add_curer")],
    ]
)
