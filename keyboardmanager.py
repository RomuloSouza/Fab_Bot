import db
from db import Product
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply

class KeyboardManager:
    
    def create_add_buttons(self, chat_id):
        """
        Creates inline keyboard buttons to insert a product to product
        """

        query = db.SESSION.query(Product).filter_by(chat=chat_id)
        products = query.all()
        keyboard_buttons = []
        for product in products:
            keyboard_buttons.append(InlineKeyboardButton(product.name, callback_data=("add " + str(product.id))))

        return [keyboard_buttons[i:i+3] for i in range(0, len(keyboard_buttons), 3)]

    def create_rm_buttons(self, chat_id):
        """
        Create inline keyboard buttons to remove product
        """

        query = db.SESSION.query(Product).filter_by(chat=chat_id)
        products = query.all()
        keyboard_buttons = []
        for product in products:
            keyboard_buttons.append(InlineKeyboardButton(product.name, callback_data=("rm " + str(product.id))))

        return [keyboard_buttons[i:i+3] for i in range(0, len(keyboard_buttons), 3)]

    def create_rm_debt_buttons(self, chat_id):
        """
        Creates inline keyboard buttons to remove from debt
        """

        query = db.SESSION.query(Product).filter_by(chat=chat_id)
        products = query.all()
        keyboard = []
        for product in products:
            if(product.quantity > 0):
                keyboard.append(InlineKeyboardButton("{} - {} - {}".format(product.name, product.price, str(product.quantity)), callback_data=("rm_debt " + str(product.id))))

        return [keyboard[i:i+3] for i in range(0, len(keyboard), 3)]