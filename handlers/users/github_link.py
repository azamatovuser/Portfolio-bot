from aiogram import types
from loader import dp, bot


@dp.message_handler(text=['Github ссылка'])
async def bot_start(message: types.Message):
    global msg
    msg = 'https://github.com/azamatovuser'
    await bot.send_message(message.chat.id, msg)