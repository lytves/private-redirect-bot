from telegram import Update
from telegram.ext import CallbackContext

from my_private_bot.config import YOUR_TELEGRAM_CHAT_ID
from my_private_bot.utils import module_logger


def start(update: Update, context: CallbackContext):
    """
     Bot's "start" command handler
    :param  update
    :param   context
    """

    usr_chat_id = update.effective_chat.id
    usr_first_name = update.message.from_user.first_name
    usr_username = "@" + update.message.from_user.username if update.message.from_user.username else ''

    msg_to_redirect = '"/start" command from: {} ({}) id: {}'.format(usr_first_name, usr_username, usr_chat_id)
    module_logger.info(msg_to_redirect)

    usr_first_name = update.message.from_user.first_name
    if update.message.from_user.last_name:
        usr_first_name += ' ' + update.message.from_user.last_name
    usr_chat_id = update.message.chat_id

    text_response = '🇷🇺 Привет, ' + usr_first_name + '. Можешь отправить мне своё сообщение.' \
                    '\n🇬🇧 Hello, ' + usr_first_name + '. Ok, send me your message now.' \
                    '\n🇪🇸 Hola, ' + usr_first_name + '. Ahora envíame tu menssaje.'

    context.bot.send_message(usr_chat_id, text_response, parse_mode="Markdown")

    context.bot.send_message(YOUR_TELEGRAM_CHAT_ID, msg_to_redirect, parse_mode="Markdown")


def filter_text_input(update: Update, context: CallbackContext):
    """
     Bot's any text message handler
    :param  update
    :param   context
    """

    if update and update.message:
        usr_chat_id = update.effective_chat.id
        usr_first_name = update.message.from_user.first_name
        usr_username = "@" + update.message.from_user.username if update.message.from_user.username else ''

        usr_msg_text = str(update.message.text) if update.message.text else '---'

        msg_to_redirect = "*{}* ({}) id: *{}* send you a message:\n{}"\
            .format(usr_first_name, usr_username, usr_chat_id, usr_msg_text)

        context.bot.send_message(YOUR_TELEGRAM_CHAT_ID, msg_to_redirect, parse_mode="Markdown")

        module_logger.info('Text "%s" from: %s (%s) id: %s',
                              usr_msg_text, usr_first_name, usr_username, usr_chat_id)
