# -*- coding: utf-8 -*-
import datetime
import time


def str_10_timestamp(time_str):
    '''
    字符串转时间戳，返回10位时间戳
    :param time_str:
    :return:
    '''
    if ':' not in time_str:
        time2 = datetime.datetime.strptime(time_str, "%Y-%m-%d")
    else:
        time2 = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    time3 = time.mktime(time2.timetuple())
    time4 = int(time3)
    return time4


# print(str_10_timestamp('2020-09-27'))

def str_13_timestamp(time_str):
    '''
    字符串转时间戳，返回13位时间戳
    :param time_str:
    :return:
    '''
    time2 = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    time3 = time.mktime(time2.timetuple())
    time4 = int(time3 * 1000)
    return time4


def timestamp_10_str(time1):
    '''
        时间戳转字符串，10位时间戳
        :param time_str:
        :return:
        '''
    time2 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time1)))
    return time2


def timestamp_13_str(time1):
    '''
         时间戳转字符串，13位时间戳
        :param time_str:
        :return:
        '''
    time2 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time1)/1000))
    return time2


# print(str_10_timestamp('2020-3-3 00:00:00'))