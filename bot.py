import asyncio
import logging
from decouple import config
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
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
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Голосовые сообщения 🎙️", callback_data="set_audio_mode")],
            [InlineKeyboardButton(text="Текстовые сообщения 📝", callback_data="set_text_mode")]
        ]
    )
    await message.answer(description, reply_markup=kb)


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


@dp.callback_query()
async def process_callback(callback_query: types.CallbackQuery):
    # Уведомление Telegram о том, что запрос обработан
    await bot.answer_callback_query(callback_query.id)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())