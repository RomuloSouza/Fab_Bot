import os
import requests

TOKEN = os.environ['BOT_API_TOKEN']

url = 'https://api.telegram.org/bot' + str(TOKEN) + '/getMe'

response = requests.get(url)
response = response.content.decode("utf8")
print('token = ' + TOKEN)
print('url = ' + url)
print('response = ' + str(response))
