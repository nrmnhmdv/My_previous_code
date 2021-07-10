from SimpleBot import Constants as keys

from telegram.ext import *

import Responses as R

print("Bot started......")

def start_command(update, context):
    update.message.reply_text('Type somting random to get started!!')

def help_command(update, context):
    update.message.reply_text('If you need help. You shuld ask for on it Google !!')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")



def main():
    updateder = Updater(keys.API, use_context=True)

    dp = updateder.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updateder.start_polling(60)
    updateder.idle()

main()
