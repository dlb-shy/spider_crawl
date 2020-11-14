# -*- coding: utf-8 -*-
import time

import requests
from requests.exceptions import ProxyError, SSLError
from urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
from settings import PROXY
from loguru import logger
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def formrequest(url, headers, formdata, timeout=30):
    '''
    POST 请求 fromdata请求
    :param url: 请求的url
    :param headers: headers
    :param formdata: 提交的数据
    :param timeout: 超时，默认30秒
    :return:
    '''
    while True:
        try:
            with requests.post(url, headers=headers, data=formdata, timeout=timeout, verify=False) as res:  # proxies=PROXY,
                logger.info(' Crawl [' + str(res.status_code) + ']: ' + url)
                return res
        except ProxyError as e:
            continue
        except SSLError as e:
            continue
        except Exception as e:
            print(e)
            return None


def payrequest(url, headers, payload, timeout=30):
    '''
    POST 请求 payload请求
    :param url: 请求的url
    :param headers: headers
    :param payload: 提交的数据
    :param timeout: 超时，默认30秒
    :return:
    '''
    while True:
        try:
            with requests.post(url, headers=headers, json=payload, timeout=timeout, verify=False) as res:  # proxies=PROXY,
                # print(res.status_code)
                # print(res.text)
                # print(res.headers)
                logger.info(' Crawl [' + str(res.status_code) + ']: ' + url)
                return res
            # del res
            # gc.collect()
        except ProxyError as e:
            continue
        except SSLError as e:
            continue
        except Exception as e:
            print(e)
            return None


def formrequest_session(url, headers, formdata, timeout=30, session=None):
    '''
        POST 请求 session请求
        :param url: 请求的url
        :param headers: headers
        :param formdata: 提交的数据
        :param timeout: 超时，默认30秒
        :return:
        '''
    while True:
        try:
            if session:
                pass
            else:
                session = requests.Session()
            res = session.post(url, headers=headers, data=formdata, timeout=timeout, verify=False)  # proxies=PROXY,
            logger.info(' Crawl [' + str(res.status_code) + ']: ' + url)
            return res
        except ProxyError as e:
            continue
        except SSLError as e:
            continue
        except Exception as e:
            print(e)
            return None