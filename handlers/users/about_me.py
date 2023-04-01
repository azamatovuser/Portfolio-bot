from aiogram import types
from keyboards.default.btn_cases import btn_cases

from loader import dp


@dp.message_handler(text=['Расcкажи о себе'])
async def bot_start(message: types.Message):
    await message.answer('Я - начинающий бэкенд-разработчик с 2022-года, '
                         'специализирующийся на использовании фреймворка Django '
                         'для создания сайтов и ботов в Telegram с помощью библиотеки '
                         'aiogram. Я владею языком программирования Python, а также '
                         'имею опыт работы с API, базами данных MySQL и PostgreSQL, '
                         'Git (на базовом уровне) и деплоем на Heroku.Мои навыки '
                         'включают создание REST API, работу с ORM Django, а также '
                         'реализацию функций авторизации и аутентификации пользователей. '
                         'Я постоянно изучаю новые технологии и стараюсь применять '
                         'их в своих проектах.', reply_markup=btn_cases)
