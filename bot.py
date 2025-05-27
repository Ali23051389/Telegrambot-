from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

# لیست آی‌دی‌های ادمین – آی‌دی خودت رو اینجا وارد کن
ADMIN_IDS = [7108445844]  # ← این عدد رو با آیدی خودت جایگزین کن

# گرفتن توکن از متغیر محیطی
TOKEN = os.environ.get("BOT_TOKEN")

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in ADMIN_IDS:
        await show_admin_panel(update, context)
    else:
        await update.message.reply_text("سلام! به ربات خوش اومدی.")

# نمایش منوی مدیریت برای ادمین
async def show_admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["مشاهده سفارش‌ها"],
        ["افزودن امتیاز به کاربر"],
        ["حذف سفارش"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("پنل مدیریت:", reply_markup=reply_markup)

# هندل کردن پیام‌های متنی
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in ADMIN_IDS:
        text = update.message.text
        if text == "مشاهده سفارش‌ها":
            await update.message.reply_text("سفارشی ثبت نشده هنوز.")
        elif text == "افزودن امتیاز به کاربر":
            await update.message.reply_text("لطفا آی‌دی و مقدار امتیاز را ارسال کنید.")
        elif text == "حذف سفارش":
            await update.message.reply_text("کد سفارش را وارد کنید.")
        else:
            await update.message.reply_text("دستور نامعتبر.")
    else:
        await update.message.reply_text("شما دسترسی به این بخش ندارید.")

# راه‌اندازی ربات
if __name__ == '__main__':
    if not TOKEN:
        print("BOT_TOKEN تعریف نشده! لطفاً توکن را در Render به عنوان Environment Variable تعریف کنید.")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        print("ربات اجرا شد.")
        app.run_polling()

