from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔍 Поиск'),
            KeyboardButton(text='🗂 Сделки')
        ],
        [
            KeyboardButton(text='🎓 Профиль'),
            KeyboardButton(text='👤 Помощь')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Тест',
    selective=True
)
