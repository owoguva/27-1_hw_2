from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)




@dp.message_handler(commands=['mem'])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://medialeaks.ru/wp-content/uploads/2022/11/snimok-ekrana-7545.jpg')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Hello world!")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer("Сам разбирайся!")


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "Вторая мировая война "
    answer = [
        "1939-1945",
        "1941-1945",
        "1916-1918",
        "1938-1945",
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Стыдно не знать",
        open_period=10,
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    question = "Кто написал произведение Евгений Онегин?"
    answer = [
        "Лермонтов",
        "Гоголь",
        "Пушкин",
        "Толстой",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=10,
    )
@dp.message_handler()
async def echo(message: types.Message):
    try:
        num = float(message.text)
        await message.answer(str(num**2))
    except ValueError:
        await message.answer(message.text)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)