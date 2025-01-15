"""
    通过threading模块实现多线程
"""
import time
import threading


def wishing(content):
    while True:
        print(content)
        time.sleep(1)


def cooking(content):
    while True:
        print(content)
        time.sleep(1)


if __name__ == '__main__':
    # wishing()
    # cooking()
    # 创建洗菜线程
    wishing_thread = threading.Thread(target=wishing, args=("洗菜菜，啦啦啦",))
    # 创建煮饭，炒菜线程
    cooking_thread = threading.Thread(target=cooking, kwargs={"content": "烧饭，炒菜，呼呼呼"})

    # 启动线程
    wishing_thread.start()
    cooking_thread.start()
