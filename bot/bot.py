
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello!')

def main() -> None:
    updater = Updater("YOUR_TELEGRAM_TOKEN")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_webhook(listen="0.0.0.0", port=443, url_path="YOUR_TELEGRAM_TOKEN")
    updater.bot.set_webhook("https://your_domain.com/" + "YOUR_TELEGRAM_TOKEN")

    updater.idle()

if __name__ == '__main__':
    main()
