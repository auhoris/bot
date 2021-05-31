from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_start = KeyboardButton('/test')
button_help = KeyboardButton('/help')
info_kb = ReplyKeyboardMarkup(resize_keyboard=True)
info_kb.add(button_start).add(button_help)

answer_kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_yes = KeyboardButton("Да")
button_no = KeyboardButton("Нет")
answer_kb.row(button_yes).row(button_no)

end_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button_end = KeyboardButton("Закончить")
end_kb.row(button_end)
