import random
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "8203972467:AAGIybKwAUrq3aIo2a9VFGDNMB4-qxsWwbU"

WELCOME_MESSAGES = [
    "🌷 {name} عزیز، به هُرمِ واژه خوش اومدی! اینجا، شعر نفس می‌کشه.",
    "🎉 {name} گرامی، محفل واژه‌ها با ورودت نورانی شد.",
    "🍃 خوش اومدی {name} جان! اینجا مأمن عاشقان شعر و احساسه.",
    "📝 {name} مهربان! واژه‌ها چشم‌به‌راه طنین حضورت بودن.",
    "📖 {name} عزیز! قدمت رو گل می‌گیریم در خانه‌ی شاعران.",
    # می‌تونی تا ۱۰۰ تا دیگه هم بهش اضافه کنی
]

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for new_user in update.message.new_chat_members:
        name = new_user.first_name
        text = random.choice(WELCOME_MESSAGES).format(name=name)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    app.run_polling()
