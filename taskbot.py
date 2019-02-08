import requests
import constants
from botapi import BotAPI

def main():

    tgAPI = BotAPI()

    url = constants.URL_TELEGRAM + '/getMe'
    url2 = constants.URL_TELEGRAM + '/getUpdates?limit=2'
    response = tgAPI.get(url)
    update = tgAPI.get(url2)
    # response = requests.get(url)
    # response = response.content.decode("utf8")
    # print('token = ' + constants.TOKEN)
    # print('url = ' + url)
    print('response = ' + str(response))
    print('updates = ' + str(update))

if __name__ == '__main__':
    main()
