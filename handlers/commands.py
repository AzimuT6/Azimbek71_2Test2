from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from config import bot

router_commands = Router()

@router_commands.message(Command('start'))
async def start_handler(message: Message):
    await message.answer('Здравствуйте')