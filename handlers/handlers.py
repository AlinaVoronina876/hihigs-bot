__all__ = [
    "router",
]

import logging
from aiogram import types, Router
from aiogram.filters import Command
from .keyboard import get_main_keyboard, keyboard_start
from db import async_session, User
from sqlalchemy import select

router=Router()


@router.message(Command(commands=["start", "status"]))
async def command_start_handler(message: types.Message):
    """Команда регистрации и справки"""

    async with async_session() as session:
        query = select(User).where(message.from_user.id == User.user_id)
        result = await session.execute(query)
        if result.scalars().all():
            info = "Чтобы продолжить, вызовите команду /status"
            await message.answer(info)
        else:
            await message.answer("Выберите роль", reply_markup=keyboard_start)

async def start_handler(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\nТвой ID: {message.from_user.id}",
                         reply_markup=get_main_keyboard())
    logging.info(f"Пользователь с id={message.from_user.id} запустил бота ")


@router.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer(text="Доступные команды:\n"
                         "/start - Начать\n"
                         "/help - Справка\n"
                         "/status - Статус")

@router.message(lambda message: message.text == "📖 О нас")
async def about_handler(message: types.Message):
    await message.answer("Это информация о нас!")

@router.message(lambda message: message.text == "👤 Профиль")
async def profile_handler(message: types.Message):
    await message.answer(f"Ваш профиль: ID {message.from_user.id}")

@router.message()
async def echo_message(message:types.Message):
    logging.debug(f"Пользователь с id={message.from_user.id} прислал необрабатываемую команду ")
    await message.answer("Неизвестная команда.Выведите /help для списка доступных")

