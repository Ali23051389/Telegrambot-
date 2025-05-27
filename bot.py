from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# لیست آی‌دی ادمین‌ها
ADMIN_IDS = [7108445844]  # اینجا آی‌دی خودت رو بذار

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in ADMIN_IDS:
        await show_admin_panel(update, context)
    else:
        await update.message.reply_text("سلام! به ربات خوش اومدی.")

# نمایش منوی ادمین
async def show_admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["مشاهده سفارش‌ها"],
        ["افزودن امتیاز به کاربر"],
        ["حذف سفارش"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("پنل مدیریت:", reply_markup=reply_markup)

# هندل کردن پیام‌ها (برای تست فقط پیام متنی)
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

# اجرای ربات
if __name__ == '__main__':
    app = ApplicationBuilder().token("توکن_ربات_تو").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("ربات اجرا شد.")
    app.run_polling()
