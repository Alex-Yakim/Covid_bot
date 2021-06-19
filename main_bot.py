from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

import config
from Parser import CovidParser


bot = Bot(token=config.token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
parser = CovidParser()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    start_buttons = ['Москва', 'Санкт-Петербург', 'Екатеринбург', 'Россия и мир']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer(
        "Привет!\n"
        "Данный бот может отправлять тебе <b>статистику по коронавирусу</b>.\n"
        "Информация о количестве:\n<i>Заболевших</i>\n<i>Выздоровевших</i>\n<i>Погибших</i>", reply_markup=keyboard
    )


@dp.message_handler(Text(equals='Москва'))
async def statistic_moscow(message: types.Message):
    data = parser.covid_moscow()
    await message.answer(f'<b>Статистика коронавируса в Москве</b>\n{data[0]}\n{data[1]}\n{data[2]}')


@dp.message_handler(Text(equals='Санкт-Петербург'))
async def statistic_moscow(message: types.Message):
    data = parser.covid_spb()
    await message.answer(f'<b>Статистика коронавируса в Санкт-Петербурге</b>\n{data[0]}\n{data[1]}\n{data[2]}')


@dp.message_handler(Text(equals='Екатеринбург'))
async def statistic_moscow(message: types.Message):
    data = parser.covid_ekb()
    await message.answer(f'<b>Статистика коронавируса в Свердловской области</b>\n{data[0]}\n{data[1]}\n{data[2]}')


@dp.message_handler(Text(equals='Россия и мир'))
async def statistic_moscow(message: types.Message):
    data = parser.covid_global()
    await message.answer(f'<b>Статистика коронавируса в России</b>\n{data[0]}\n{data[1]}\n{data[2]}\n\n'
                         f'<b>Статистика коронавируса в мире</b>\n{data[3]}')


if __name__ == '__main__':
    executor.start_polling(dp)
    print('Bot started')
