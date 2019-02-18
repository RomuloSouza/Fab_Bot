#!/usr/bin/env python3.6.7
# -*- coding: utf-8 -*-
import logging
import db
import constants
from util import isfloat
from db import Cart
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class BotManager:
    """
    Define all commands used in the bot
    """

    def start(self, bot, update):
        # keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
        #             InlineKeyboardButton("Option 2", callback_data='2')],

        #             [InlineKeyboardButton("Option 3", callback_data='3')]]

        # reply_markup = InlineKeyboardMarkup(keyboard)

        reply_markup = ForceReply()

        update.message.reply_text('Please choose:', reply_markup=reply_markup)


    def call_back(self, bot, update):
        """
        Represents an incoming callback query from a callback button in an inline keyboard.
        """

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
        elif(method == "rm"):
            query_db = db.SESSION.query(Cart).filter_by(id=int(option))
            cart = query_db.one()
            db.SESSION.delete(cart)
            db.SESSION.commit()

            bot.edit_message_text(text="{} successfully removed.".format(cart.name),
                                chat_id=query.message.chat_id,
                                message_id=query.message.message_id)
        elif(method == "rm_dept"):
            query_db = db.SESSION.query(Cart).filter_by(id=int(option))
            cart = query_db.one()
            cart.quantity = cart.quantity - 1
            db.SESSION.commit()

            bot.edit_message_text(text="A paid {}. You should {}".format(cart.name, cart.quantity),
                                chat_id=query.message.chat_id,
                                message_id=query.message.message_id)

    def list_cart(self, bot, update):
        """
        List all products linked to chat
        """

        query = db.SESSION.query(Cart).filter_by(chat=update.message.chat.id)
        cart = query.all()
        text = "Products\n"
        for i in cart:
            text += i.name + " - " + i.price + "\n"

        update.message.reply_text(text)

    def new_product(self, bot, update):
        """
        Insert a product into the database linked to chat
        """

        text = update.message.text
        commands = text.split(" ")
        if(len(commands) >= 3 and isfloat(commands[-1])):
            name = " ".join(commands[1:-1])
            price = commands[-1]

            cart = Cart(chat=update.message.chat.id, name=name, price=price, quantity=0)
            db.SESSION.add(cart)
            db.SESSION.commit()
            update.message.reply_text("Procuct succesfully added")

    def remove_product(self, bot, update):
        """
        Remove a product into the database linked to chat
        """

        keyboard = self.create_rm_buttons(update.message.chat.id)
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text("Please choose a product:", reply_markup=reply_markup)

    def fab_products(self, bot, update):
        """
        Add all products used in FSW
        """
        
        # TODO - Add all products
        cart = Cart(chat=update.message.chat.id, name="Guarana", price="1.50", quantity=0)
        db.SESSION.add(cart)
        db.SESSION.commit()
        update.message.reply_text("Products successfully added")

    def add_to_cart(self, bot, update):
        """
        Add a product to the account
        """
        
        keyboard = self.create_add_buttons(update.message.chat.id)
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text("Please choose a product:", reply_markup=reply_markup)

    def remove_to_cart(self, bot, update):
        """
        Remove a product to the acount
        """

        keyboard = self.create_rm_dept_buttons(update.message.chat.id)
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text("Please choose a dept:", reply_markup=reply_markup)

    def help(self, bot, update):
        """
        Reply to user all commands used in the bot 
        """

        update.message.reply_text(constants.HELP)


    def error(self, bot, update, error):
        """
        Log Errors caused by Updates.
        """

        logger.warning('Update "%s" caused error "%s"', update, error)

    def create_add_buttons(self, chat_id):
        """
        Create inline keyboard buttons to insert a cart
        """

        query = db.SESSION.query(Cart).filter_by(chat=chat_id)
        products = query.all()
        keyboard_buttons = []
        for product in products:
            keyboard_buttons.append(InlineKeyboardButton(product.name, callback_data=("add " + str(product.id))))

        return [keyboard_buttons[i:i+3] for i in range(0, len(keyboard_buttons), 3)]

    def create_rm_buttons(self, chat_id):
        """
        Create inline keyboard buttons to remove product
        """

        query = db.SESSION.query(Cart).filter_by(chat=chat_id)
        products = query.all()
        keyboard_buttons = []
        for product in products:
            keyboard_buttons.append(InlineKeyboardButton(product.name,callback_data=("rm " + str(product.id))))

        return [keyboard_buttons[i:i+3] for i in range(0, len(keyboard_buttons), 3)]

    def create_rm_dept_buttons(self, chat_id):
        """
        Create inline keyboard buttons to remove from dept
        """

        query = db.SESSION.query(Cart).filter_by(chat=chat_id)
        products = query.all()
        keyboard = []
        for product in products:
            if(product.quantity > 0):
                keyboard.append(InlineKeyboardButton("{} - {} - {}".format(product.name, product.price, str(product.quantity)), callback_data=("rm_dept " + str(product.id))))

        return [keyboard[i:i+3] for i in range(0, len(keyboard), 3)]
