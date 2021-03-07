from collections import UserDict


class ShortUrlsStorage(UserDict):

    def to_key(self, url):
        return url

    def to_long(self, key):
        pass
        # return 'http://yandex.ru'

shorts = ShortUrlsStorage()
