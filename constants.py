import os

TOKEN = os.environ['BOT_API_TOKEN']
URL_TELEGRAM = 'https://api.telegram.org/bot'+ str(TOKEN)
HELP = """
You can control me by sending these commands:
 /list - list all products
 /debt - list your debt and values
 /buy - add a product to your debt
 /pay - remove a product from your debt
 /newProd - create a new product
 /rmProd - delete a product
"""