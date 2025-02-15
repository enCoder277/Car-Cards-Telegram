import asyncio
import logging
from decouple import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# логи
logging.basicConfig(level=logging.INFO)
BOT_TOKEN = config('TELEGRAM_BOT_TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    description = (
        "Привет, коллекционер! 🚗\n"
        "Добро пожаловать в бота для коллекционирования карточек машин!\n"
        "Чтобы ознакомиться с возможностями бота, нажми на команду /manual"
    )
    kb = [
        [
            types.KeyboardButton(text="Пример 1"),
            types.KeyboardButton(text="Пример 2")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери действие"
    )
    await message.answer(description, reply_markup=keyboard)


@dp.message(Command("manual"))
async def cmd_manual(message: types.Message):
    help_text = (
        "manual cmd"
    )

    await message.answer(help_text)


@dp.message(Command("collection"))
async def cmd_collection(message: types.Message):
    description = (
        "collection"
    )
    await message.answer(description)


@dp.message(Command("add_to_collection"))
async def cmd_add_to_collection(message: types.Message):
    description = (
        "add_to_collection"
    )
    await message.answer(description)


@dp.message(Command("deck"))
async def cmd_deck(message: types.Message):
    description = (
        "deck"
    )
    await message.answer(description)


@dp.message(Command("support_project"))
async def cmd_support_project(message: types.Message):
    description = (
        "support_project"
    )
    await message.answer(description)


BUTTON_TEXTS = {"Пример 1", "Пример 2"}

@dp.message_handler(lambda message: message.text in BUTTON_TEXTS)
async def handle_buttons(message: types.Message):
    if message.text == "Пример 1":
        await message.answer("Вы нажали кнопку 'Пример 1'")
    elif message.text == "Пример 2":
        await message.answer("Вы нажали кнопку 'Пример 2'")
    elif message.text == "Другая кнопка":
        await message.answer("Вы нажали кнопку 'Другая кнопка'")
    elif message.text == "Еще кнопка":
        await message.answer("Вы нажали кнопку 'Еще кнопка'")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())