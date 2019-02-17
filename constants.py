import os

TOKEN = os.environ['BOT_API_TOKEN']
URL_TELEGRAM = 'https://api.telegram.org/bot'+ str(TOKEN)
HELP = """
You can control me by sending these commands:
 /list - list all products
 /dept - list your depts and values
 /add - add a product to dept
 /pay - remove a product to dept
 /newProd - create a new product
 /rmProd - delete a product
"""