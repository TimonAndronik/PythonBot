from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "7799928283:AAESCCosJnkx9NRR6D-PwKT9gIBFdFAWrqs"


async def start(update: Update, context):
    await update.message.reply_text("Привіт! Я простий бот. Напиши щось!")


async def help_command(update: Update, context):
    await update.message.reply_text("Я просто повторюю твої повідомлення. Спробуй!")


async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Бот запущено...")
    app.run_polling()


if __name__ == "__main__":
    main()
