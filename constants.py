import os

TOKEN = os.environ['BOT_API_TOKEN']
URL_TELEGRAM = 'https://api.telegram.org/bot'+ str(TOKEN)
HELP = """
You can control me by sending these commands:
 /list - list all products
 /debt - list your debts and values
 /add - add a product to debt
 /pay - remove a product to debt
 /newProd - create a new product
 /rmProd - delete a product
"""