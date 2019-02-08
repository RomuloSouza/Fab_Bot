import requests
import constants
from botapi import BotAPI

def main():
    bot_api = BotAPI()
    offset = None

    while True:
        updates = bot_api.get_updates(offset)
        if updates['result']:
            offset = bot_api.get_last_update_id(updates)+1
            for i in updates['result']:
                bot_api.send_message(i['message']['chat']['id'], "Hellou romulo, como vc esta?")
        print('response = ' + str(updates))        

if __name__ == '__main__':
    main()
