from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.btn_about import btn_about

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\nЯ бот, который позволит тебе узнать чуть больше обо мне", reply_markup=btn_about)
