from aiogram import types
from keyboards.default.all_cases import all_cases

from loader import dp


@dp.message_handler(text=['Мои кейсы'])
async def bot_start(message: types.Message):
    await message.answer('Выбирай, какой проект тебе интересен?' ,reply_markup=all_cases)