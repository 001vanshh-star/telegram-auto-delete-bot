from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")

async def delete_edited(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.edited_message:
        await asyncio.sleep(6)
        await update.edited_message.delete()

async def delete_links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and ("http" in update.message.text or "t.me" in update.message.text):
        await update.message.delete()

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, delete_edited))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, delete_links))

print("Bot running...")
app.run_polling()
