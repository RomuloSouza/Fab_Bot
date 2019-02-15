#!/usr/bin/env python3.6.7
# -*- coding: utf-8 -*-
"""Basic example for a bot that uses inline keyboards.
# This program is dedicated to the public domain under the CC0 license.
"""
import constants
from botmanager import BotManager
from db import Cart
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(constants.TOKEN)
    bot_manager = BotManager()

    updater.dispatcher.add_handler(CommandHandler('start', bot_manager.start))
    updater.dispatcher.add_handler(CommandHandler('new', bot_manager.new_product))
    updater.dispatcher.add_handler(CommandHandler('list', bot_manager.list_cart))
    updater.dispatcher.add_handler(CallbackQueryHandler(bot_manager.button))
    updater.dispatcher.add_handler(CommandHandler('help', bot_manager.help))
    updater.dispatcher.add_error_handler(bot_manager.error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()