# spider_crawl1.0（2020-11-14）
多线程+requests的微爬虫框架

## 组成

spider

    ├── __pycache__

    │   └── settings.cpython-37.pyc

    ├── piplelines

    │   └── __init__.py

    ├── requirements.txt

    ├── run.py

    ├── scheduler

    │   ├── __init__.py

    │   ├── __pycache__

    │   │   ├── __init__.cpython-37.pyc

    │   │   └── scheduler.cpython-37.pyc

    │   ├── baijiaohao_s.py

    │   └── scheduler.py

    ├── settings.py

    ├── shttp

    │   ├── __init__.py

    │   ├── __pycache__

    │   │   ├── __init__.cpython-37.pyc

    │   │   ├── get.cpython-37.pyc

    │   │   └── post.cpython-37.pyc

    │   ├── get.py

    │   └── post.py

    ├── spider

    │   ├── __init__.py

    │   ├── __pycache__

    │   │   └── __init__.cpython-37.pyc

    │   └── baijiahao_inl.py

    └── util

    ├── __init__.py
    
    ├── __pycache__
    
    │   └── __init__.cpython-37.pyc
    
    └── date_util.py
    
1.scheduler--调度器
    可以通过自定义调度方法，线程数来编写调度文件
    
2.shttp--下载器
    通过封装requests完成get post 常用请求，支持session
    
3.pipelines--存储器
    可以自定义保存数据方法
    
4.spider--爬虫的主要逻辑编写
    自定义抓取方式，解析数据
    
# 优点
采用线程池方法启动爬虫，可以一次性添加任务，也可以通过判断空闲进程数添加任务

# 启动方法
在run.py中引入你自己定义的调度器，例如(baijiahao_s.py) ,开始进行抓取
