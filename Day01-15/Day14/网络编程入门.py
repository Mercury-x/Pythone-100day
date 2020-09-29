import requests
from threading import Thread


class DownloadPic(Thread):
    def __init__(self, url):
        super().__init__()
        self._url = url

    def run(self):
        filename = self._url[self._url.rfind('/') + 1:]
        resp = requests.get(self._url)
        with open('../Day14/Pics/' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    param = {
        'key': '0b20d08727c6ac912666f61de72bcf71'
    }
    resp = requests.get('http://api.tianapi.com/woman/index', params=param)
    data_model = resp.json()
    for data_url in data_model['newslist']:
        url = data_url['picUrl']
        DownloadPic(url).run()
    pass


if __name__ == "__main__":
    main()
