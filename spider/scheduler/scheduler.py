# -*- coding: utf-8 -*-
import queue
import threading
import contextlib
import time
from loguru import logger
# 空对象,用于停止线程
StopEvent = object()


def callback(status, result):
    """
    任务执行完毕后返回结果的处理方法:
    :param status: action函数的执行状态
    :param result: action函数的返回值
    :return None
    """
    logger.info("status: %s result: %s" % (status, result))


class ThreadPool:

    def __init__(self, max_thread_num, max_task_num=None):
        """
        Args:
            max_num: 线程池最大线程数
            max_task_num: 任务队列最大长度
        """
        # 如果设置了max_task_num,则任务队列最大长度为max_task_num,
        # 否则, 任务队列默认长度无限制。
        if max_task_num:
            self.q = queue.Queue(max_task_num)
        else:
            self.q = queue.Queue()
        # 最大线程数
        self.max_thread_num = max_thread_num
        # 取消任务信号
        self.cancel = False
        # 中断任务信号
        self.terminal = False
        # 执行任务的线程列表
        self.thread_running_list = []
        # 空闲状态的线程列表
        self.thread_free_list = []

    def put(self, func, args, callback_func=None):
        """
        往任务队列里放入一个任务
        Args:
            func: 任务执行方法
            args: 任务方法的参数
            callback_func: 任务执行完毕回调方法
        """
        # 添加任务之前, 先检查任务取消信号，如果取消则不再添加
        if self.cancel:
            return
        # 如果没有空闲线程，且线程数没超过最大值，则创建新线程。
        if len(self.thread_free_list) == 0 and len(self.thread_running_list) < self.max_thread_num:
            self.create_thread()

        # 构造任务
        w = (func, args, callback_func)
        # 放进任务队列
        self.q.put(w)

    def create_thread(self):
        """
        创建一个线程，此线程执行本类call()方法
        """
        t = threading.Thread(target=self.call)
        t.start()

    def call(self):
        """
        此方法作为线程启动，启动后将自己加入线程列表中，并从任务队列获取一个任务。
        如果任务不是空对象，则开始执行此任务。
        一个任务执行完毕，将暂时把自己放到空闲线程列表中，并开始等待获取下一个任务。
        self.q.get() 是阻塞的，任务列表中没有任务将一直等待，直到获取到任务，或者接收到停止标识对象则关闭线程。
        """
        # 当前线程名
        current_thread = threading.currentThread().getName()
        # 追加到线程列表
        self.thread_running_list.append(current_thread)
        # 获取任务
        event = self.q.get()
        while event != StopEvent:
            # 解析任务中封装的三个参数
            func, arguments, callback = event
            # 防止任务异常导致线程关闭，用try...except... 执行任务。
            # print(*arguments, )
            try:
                result = func(*arguments)
                # print('---', result)
                success = True
            except Exception as e:
                # print('---', e)
                result = None
                success = False
            # 回调方法不为 None 时,执行回调方法。同样用try...except...
            if callback is not None:
                try:
                    callback(success, result)
                except Exception as e:
                    logger.info('callback %s run failed, err: %s .' % (callback, e))

            # 完成任务, 执行self.worker_state 方法，将自己加入空闲线程列表, 执行yield等待。
            # 直到此下self.q.get() 获取新任务切换到yield下一条代码将自身从空闲线程移除。并继续执行循环
            with self.worker_state(self.thread_free_list, current_thread):
                # 通过self.terminal 强制关闭线程
                if self.terminal:
                    event = StopEvent
                else:
                    event = self.q.get()

        else:
            # 获取到结束标识对象， 将自身从线程列表中移除，并结束本线程。
            self.thread_running_list.remove(current_thread)

    def close(self):
        """
        关闭所有线程,等待已入队列的任务执行完毕
        """
        # 设置此标识， 停止self.put()添加任务
        self.cancel = True

        # 向任务队列中添加与线程相同数量的StopEvent,停掉所有线程。
        size = len(self.thread_running_list)
        while size:
            self.q.put(StopEvent)
            size -= 1

    def terminate(self):
        """
        强制关闭线程，已入待队列任务不在处理。
        """
        # 停止self.put() 添加任务
        self.cancel = True
        # 停止执行任务
        self.terminal = True

        # 通知线程关闭
        while self.thread_running_list:
            self.q.put(StopEvent)

    # 该装饰器用于上下文切换管理
    @contextlib.contextmanager
    def worker_state(self, state_list, worker_thread):
        """
        管理空闲线程列表
        """
        # 将当前线程，添加到空闲线程列表中
        state_list.append(worker_thread)
        try:
            yield  # 等待
        finally:
            # 切换回来时 从空闲列表删除线程
            state_list.remove(worker_thread)


# if __name__ == '__main__':
#     # 创建线程池实例,最大线程数5个。
#     pool = ThreadPool(5)
#     # 向任务队列赛100个任务
#     for i in range(100):
#         pool.put(action, (i,), callback)
#     # 等待一定时间，让线程执行任务
#     # 正常关闭线程池
#     pool.close()
#     # 强制关闭线程池
    # pool.terminate()





