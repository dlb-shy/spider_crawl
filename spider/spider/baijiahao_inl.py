# -*- coding: utf-8 -*-

from shttp.get import request




headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36',
}


def start_requests(data):
    url = data['url']
    response = request(url, headers=headers)
    parse(response)


def parse(response):
    print(response.status_code)
    print(response.text)




# if __name__ == '__main__':
#     data = {}
#     start_requests(data)