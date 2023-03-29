from aiogram import Bot, types, utils
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = ''
URL_APP = ''

bot = Bot(token=TOKEN)
dp =Dispatcher(bot)

async def onstartup(dp):
    print('Бот запущен')
    await bot.set_webhook(URL_APP)


@dp.message_handler()
async def str(msg : types.Message):
    await msg.answer("Привет")

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True, on_startup=onstartup)

