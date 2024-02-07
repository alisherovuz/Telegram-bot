from aiogram import Bot, Dispatcher, types
from config import TOKEN
from aiogram.filters import CommandStart
import asyncio
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
        await message.answer('hello')


#@dp.message()
#async def start_cmd(message: types.Message):
#    await message.answer(message.text)

@dp.message()
async def avto(message: types.Message):
    matn = message.text
    if matn == 'qalaysan':
        await message.answer("rahmat, o'zingchi?")
    elif matn == 'Nima gaplar':
        await message.answer("Tinchlik")

    elif matn == "Men necha yoshman?":
        await message.answer('15')


async def main():
    await dp.start_polling(bot)


asyncio.run(main())