# -*- coding: utf-8 -*-
import json
import time
from loguru import logger
from scheduler.scheduler import ThreadPool, callback
from settings import PROXY
from spider.baijiahao_inl import start_requests

TYPE_NAME = ''
REQUEST_COUNT = 10  # 并发线程数
TASK_COUNT = 50


def start():
    # 一次性所有任务进入队列
    pool = ThreadPool(REQUEST_COUNT)
    datas = [{'url': 'http://www.baidu.com'}]
    for data in datas:
        pool.put(start_requests, (data,))
    pool.close()
    # # 可以在程序执行中添加新的任务
    # pool = ThreadPool(REQUEST_COUNT)
    # flag = 0
    # while True:
    #     time.sleep(0.1)
    #     if flag == 0:
    #         datas = get_task(TYPE_NAME, req_count=TASK_COUNT)
    #         print(datas)
    #         if datas:
    #             for data in datas:
    #                 data = json.loads(data)
    #                 pool.put(start_requests, (data,))
    #         flag = 1
    #     logger.info('正在工作的线程 ' + str(len(pool.thread_running_list)) + ' 空闲的线程 ' + str(len(pool.thread_free_list)))
    #     if len(pool.thread_free_list) > 0:
    #         datas = get_task(TYPE_NAME, req_count=TASK_COUNT)
    #         print(datas)
    #         if datas:
    #             for data in datas:
    #                 data = json.loads(data)
    #                 pool.put(start_requests, (data,))
    #         else:
    #             time.sleep(5)
    #     else:
    #         time.sleep(5)
    # pool.close()