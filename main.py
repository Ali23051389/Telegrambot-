from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters
)
import os

# توکن ربات و URL دامنه سرور رندر
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # مثلا: https://your-app-name.onrender.com/webhook

# پاسخ ساده
def ai_response(text):
    text = text.lower()
    if "سلام" in text:
        return "سلام! خوش اومدی."
    elif "چطوری" in text:
        return "من خوبم، تو چطوری؟"
    else:
        return "فعلاً چیز زیادی بلد نیستم!"

# هندل پیام‌ها
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    reply = ai_response(user_message)
    await update.message.reply_text(reply)

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من یه ربات ساده‌ام. باهام حرف بزن!")

# تابع راه‌اندازی ربات
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # تنظیم webhook
    await app.bot.set_webhook(url=WEBHOOK_URL)

    # اجرای webhook سرور
    await app.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 8080)),
        webhook_url=WEBHOOK_URL,
    )

if __name__ == __main__:
    import asyncio
    asyncio.run(main())