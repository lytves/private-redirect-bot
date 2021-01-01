from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters

from my_private_bot.config import TOKEN_BOT
from my_private_bot.handlers import start, filter_text_input
from my_private_bot.utils import module_logger


def main():
    module_logger.info("Start the @NoSleepingBot bot!")

    # create an object "bot"
    updater = Updater(token=TOKEN_BOT, use_context=True)
    dispatcher = updater.dispatcher

    # bot's start command handlers
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # bot's text handler
    text_update_handler = MessageHandler(Filters.text, filter_text_input)
    dispatcher.add_handler(text_update_handler)

    # Start the Bot start_polling() method
    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()