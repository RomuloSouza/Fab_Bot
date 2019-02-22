import db
from db import Product

class DbManager():

    def remove_products(self, chat_id):
        query_db = db.SESSION.query(Product).filter_by(chat=int(chat_id))
        products = query_db.all()
        for i in products:
            db.SESSION.delete(i)

        db.SESSION.commit()
    
    def pay_debt(self, chat_id):
        query_db = db.SESSION.query(Product).filter_by(chat=int(chat_id))
        products = query_db.all()
        for i in products:
            i.quantity = 0
        
        db.SESSION.commit()