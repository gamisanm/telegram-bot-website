from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from .config import WEBSITE_URL

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Перейдите на сайт: {WEBSITE_URL}")

def setup_bot(token):
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    return application