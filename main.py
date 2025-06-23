import asyncio
from bot.bot import setup_bot
from bot.config import BOT_TOKEN

async def main():
    bot = setup_bot(BOT_TOKEN)
    await bot.run_polling()

if __name__ == "__main__":
    asyncio.run(main())