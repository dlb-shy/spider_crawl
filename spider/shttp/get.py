# -*- coding: utf-8 -*-
import time

import requests
from requests.exceptions import ProxyError, SSLError
from urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
from settings import PROXY

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
adapter = requests.adapters.HTTPAdapter(pool_connections=1, pool_maxsize=20, max_retries=5)


def request(url, headers, timeout=30):
    '''
    GET session请求
    :param url:
    :param headers:
    :param timeout:
    :param session:
    :return:
    '''
    while True:
        try:
            with requests.get(url, headers=headers, timeout=timeout, verify=False) as res:  # proxies=PROXY,

                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ' Crawl [' + str(res.status_code) + ']: ' + url)
                return res

        except ProxyError as e:
            continue
        except SSLError as e:
            continue
        except Exception as e:
            print(e)
            return None


def request_session(url, headers, timeout=30, session=None):
    '''
    GET session请求
    :param url:
    :param headers:
    :param timeout:
    :param session:
    :return:
    '''
    while True:
        try:
            if session:
                pass
            else:
                session = requests.Session()
            res = session.get(url, headers=headers, timeout=timeout, verify=False)  # proxies=PROXY,
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ' Crawl [' + str(res.status_code) + ']: ' + url)
            return res
        except ProxyError as e:
            continue
        except SSLError as e:
            continue
        except Exception as e:
            print(e)
            return None
