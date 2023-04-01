from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from loader import dp, bot


@dp.message_handler(text=['Контакты'])
async def bot_start(message: types.Message):
    global pict, msg
    pict = open('images/logo.jpg', 'rb')
    msg = '<a href="https://github.com/azamatovuser">Github</a>  |  ' \
          '<a href="https://www.linkedin.com/in/azamat-azamatov-90392526a/">Linkedin</a>  |  ' \
          '<a href="https://t.me/azamatovhere">Telegram</a>'
    await bot.send_photo(message.chat.id, pict, caption=msg, reply_markup=ReplyKeyboardRemove())