from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from config import BOT_TOKEN
from database import connect_db
import handlers.start as start_handler
import handlers.team as team_handler
import handlers.pack as pack_handler
import handlers.match as match_handler

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
pool = None

@dp.message_handler(commands=['start'])
async def handle_start(message: Message):
    await start_handler.start_cmd(message, pool)

@dp.message_handler(commands=['team'])
async def handle_team(message: Message):
    await team_handler.show_team(message, pool)

@dp.message_handler(commands=['openpack'])
async def handle_pack(message: Message):
    await pack_handler.open_pack(message, pool)

@dp.message_handler(commands=['match'])
async def handle_match(message: Message):
    await match_handler.play_match(message, pool)

async def on_startup(dp):
    global pool
    pool = await connect_db()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
