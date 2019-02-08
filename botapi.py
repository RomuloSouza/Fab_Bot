import requests

class BotAPI():

    def get(self, url):
        response = requests.get(url)
        content = response.content.decode("utf8")
        return content
