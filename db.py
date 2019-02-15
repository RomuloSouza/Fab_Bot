#!/usr/bin/env python3.6.7

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db.sqlite3', echo=True)
SESSION = sessionmaker(bind=engine)
SESSION = SESSION()

Base = declarative_base()


class Cart(Base):
    __tablename__ = 'cart'

    id = Column(Integer, primary_key=True)
    chat = Column(Integer)
    name = Column(String)
    price = Column(String)
    quantity = Column(Integer)

    def __repr__(self):
        return "pro romulo perceber que funciona <Cart(id={}, chat={}, name='{}', price='{}')>".format(
            self.id, self.chat, self.name, self.price
        )


Base.metadata.create_all(engine)

if __name__ == '__main__':
    pass
