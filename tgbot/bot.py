import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.markdown import hbold
from aiogram.filters import Command
from aiogram import Router

TOKEN = "7673598739:AAGGQlg-mJJqJ2eOZx1egeL6043JYXugvuw"

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()  # Новый объект для хэндлеров
dp.include_router(router)  # Подключаем роутер к диспетчеру

# 🎛 Создаём правильную клавиатуру
kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет 👋"),KeyboardButton(text="Qalesan")]
    ],
    resize_keyboard=True
)

# Обработчик команды /start
@router.message(Command("start"))  # <-- В aiogram v3 так!
async def start_handler(message: types.Message):
    await message.answer(f"Привет, {hbold(message.from_user.first_name)}! Выбери кнопку:", reply_markup=kb)

# Обработчик кнопки "Привет"
@router.message(lambda message: message.text == "Привет 👋")
async def hello_handler(message: types.Message):
    await message.answer("Привет! Рад тебя видеть! 😊")

# Обработчик кнопки "Как дела?"
@router.message(lambda message: message.text == "Qalesan")
async def how_are_you_handler(message: types.Message):
    await message.answer("Harosh babiram ozbek sila (q)o'toq")

# Функция для запуска бота
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
