#!/usr/bin/env python3.6.7
# -*- coding: utf-8 -*-
import logging
import db
from db import Cart
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class BotManager:
    def start(self, bot, update):
        print(bot)
        print(update)
        keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                    InlineKeyboardButton("Option 2", callback_data='2')],

                    [InlineKeyboardButton("Option 3", callback_data='3')]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose:', reply_markup=reply_markup)


    def button(self, bot, update):
        print("\n\n")
        print(update)
        query = update.callback_query

        bot.edit_message_text(text="Selected option: {}".format(query.data),
                            chat_id=query.message.chat_id,
                            message_id=query.message.message_id)

    def list_cart(self, bot, update):
        query = db.SESSION.query(Cart).filter_by(chat=update.message.chat.id)
        cart = query.all()
        print(cart)
        text = "Products\n"
        for i in cart:
            text += i.name + " - " + i.price + "\n"
            print(i.id)
        update.message.reply_text(text)

    def new_product(self, bot, update):
        print("\n\n\n\n")
        print(update)
        print(update.message.chat.id)
        cart = Cart(chat=update.message.chat.id, name=update.message.text, price="2.50", quantity=0)
        db.SESSION.add(cart)
        db.SESSION.commit()
        update.message.reply_text("Added")

    def help(self, bot, update):
        update.message.reply_text("Use /start to test this bot.")


    def error(self, bot, update, error):
        """Log Errors caused by Updates."""
        logger.warning('Update "%s" caused error "%s"', update, error)

