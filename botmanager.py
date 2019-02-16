#!/usr/bin/env python3.6.7
# -*- coding: utf-8 -*-
import logging
import db
from db import Cart
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Bot


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class BotManager:
    def start(self, bot, update):
        keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                    InlineKeyboardButton("Option 2", callback_data='2')],

                    [InlineKeyboardButton("Option 3", callback_data='3')]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose:', reply_markup=reply_markup)


    def call_back(self, bot, update):
        query = update.callback_query
        method, option = query.data.split(" ")
        if(method == "add"):
            query_db = db.SESSION.query(Cart).filter_by(id=int(option))
            cart = query_db.one()
            cart.quantity = cart.quantity + 1
            db.SESSION.commit()

            bot.edit_message_text(text="{} successfully added. You should {}".format(cart.name, cart.quantity),
                                chat_id=query.message.chat_id,
                                message_id=query.message.message_id)

    def list_cart(self, bot, update):
        """List all products linked to chat"""
        query = db.SESSION.query(Cart).filter_by(chat=update.message.chat.id)
        cart = query.all()
        text = "Products\n"
        for i in cart:
            text += i.name + " - " + i.price + "\n"

        update.message.reply_text(text)

    def new_product(self, bot, update):
        """Insert ap product into the database linked to chat"""
        cart = Cart(chat=update.message.chat.id, name=update.message.text, price="2.50", quantity=0)
        db.SESSION.add(cart)
        db.SESSION.commit()
        update.message.reply_text("Procuct succesfully added")

    def fab_products(self, bot, update):
        """Add all products used in FSW"""
        # TODO - Add all products
        cart = Cart(chat=update.message.chat.id, name="Guarana", price="1.50", quantity=0)
        db.SESSION.add(cart)
        db.SESSION.commit()
        update.message.reply_text("Products successfully added")

    def add_to_cart(self, bot, update):
        """Add a product to the account"""
        keyboard = self.create_buttons(update.message.chat.id)
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text("Please choose a product:", reply_markup=reply_markup)

    def help(self, bot, update):
        update.message.reply_text("Use /start to test this bot.")


    def error(self, bot, update, error):
        """Log Errors caused by Updates."""
        logger.warning('Update "%s" caused error "%s"', update, error)

    def create_buttons(self, chat_id):
        """Create inline keyboard buttons"""
        query = db.SESSION.query(Cart).filter_by(chat=chat_id)
        products = query.all()
        keyboard_buttons = []
        for product in products:
            keyboard_buttons.append(InlineKeyboardButton(product.name, callback_data=("add " + str(product.id))))

        return [keyboard_buttons[i:i+3] for i in range(0, len(keyboard_buttons), 3)]