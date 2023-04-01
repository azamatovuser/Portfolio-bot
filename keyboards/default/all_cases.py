from aiogram.types import ReplyKeyboardMarkup

all_cases = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
all_cases.add('SeeFood', 'Project', 'University')
all_cases.add('Назад', 'Контакты')