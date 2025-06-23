from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from .config import BOT_TOKEN, WEBSITE_URL

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="Открыть Web App", web_app=types.WebAppInfo(url=WEBSITE_URL))]
    ])
    await message.answer("Нажмите кнопку, чтобы открыть Web App:", reply_markup=keyboard)

async def start_bot():
    await dp.start_polling(bot)