import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from app.yandex_api import get_campaigns

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой рекламный ассистент.")

async def campaigns(update: Update, context: ContextTypes.DEFAULT_TYPE):
    campaigns = get_campaigns()
    await update.message.reply_text(f"Кампании: {campaigns}")

def start_bot():
    from dotenv import load_dotenv
    load_dotenv()
    token = os.getenv("8053682328:AAFT1LVMUEUNjhcL681WVvhNniveLwftKHQ")

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("campaigns", campaigns))

    app.run_polling()
