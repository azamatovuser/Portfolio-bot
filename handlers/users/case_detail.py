from aiogram import types
from keyboards.default.btn_back import btn_back

from loader import dp


@dp.message_handler(text=['SeeFood'])
async def bot_start(message: types.Message):
    await message.answer('Этот Telegram бот, созданный на Python с помощью библиотеки aiogram, '
                         'имеет удобную функцию корзины для заказов. Пользователи могут просмотреть '
                         'свои заказы, удалить их или оформить новый заказ. Кроме того, бот также '
                         'предоставляет возможность просматривать фаст фуды с изображениями и '
                         'добавлять их в корзину. В целом, этот бот помогает упростить процесс '
                         'заказа еды через Telegram.Затраченное время на создание этого '
                         'проекта составило полмесяца.\n\nhttps://github.com/azamatovuser/seefoodproject', reply_markup=btn_back)


@dp.message_handler(text=['Project'])
async def bot_start(message: types.Message):
    await message.answer('Project, созданный с использованием библиотеки aiogram, позволяет '
                         'посетителям просматривать доступные онлайн-курсы и получать информацию'
                         'о них, в том числе цены. Посетители также могут оставлять заявки на '
                         'курсы через электронную почту. Бот предназначен для упрощения процесса '
                         'покупки онлайн-курсов. На разработку этого проекта ушло примерно 8 дней'
                         '\n\nhttps://github.com/azamatovuser/Project',
                         reply_markup=btn_back)


@dp.message_handler(text=['University'])
async def bot_start(message: types.Message):
    await message.answer('Разработанный с помощью framework Django проект представляет собой '
                         'онлайн-платформу для обучения, на которой пользователи могут выбирать '
                         'курсы в различных категориях, просматривать их описание, содержание '
                         'и цену. Пользователи могут зарегистрироваться на платформе и '
                         'просматривать приобретенные ими курсы. Также на платформе доступна'
                         'возможность оставить заявку на обучение и контактную информацию.'
                         'Для удобства пользователей предусмотрены функции поиска и фильтрации '
                         'по категориям и тегам для быстрого доступа к нужным курсам.'
                         '\n\nhttps://github.com/azamatovuser/Backend-Projects/tree/main/Education',
                         reply_markup=btn_back)