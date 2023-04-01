from aiogram import types
from keyboards.default.btn_cases import btn_cases

from loader import dp


@dp.message_handler(text=['Назад'])
async def bot_start(message: types.Message):
    await message.answer('Вы вернулись назад', reply_markup=btn_cases)