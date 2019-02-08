import constants
import requests
import json
import urllib

class BotAPI():

    def get(self, url):
        '''get response content of given url'''
        response = requests.get(url)
        content = response.content.decode("utf8")
        return content

    def get_json(self, url):
        content = self.get(url)
        payload = json.loads(content)
        return payload

    def get_updates(self, offset=None):
        url = constants.URL_TELEGRAM + '/getUpdates?timeout=100'
        if offset:
            url += '&offset={}'.format(offset)
        return self.get_json(url)

    def get_last_update_id(self, updates):
        update_ids = []
        for update in updates['result']:
            update_ids.append(int(update['update_id']))
        return max(update_ids)

    def send_message(self, chat_id, text):
        # text = urllib.parse.quote_plus(text)
        print("chat_id = {}".format(chat_id))
        print("text = {}".format(text))
        url = constants.URL_TELEGRAM + '/sendMessage?chat_id={}&text={}'.format(chat_id,text)
        print(url)
        self.get(url)