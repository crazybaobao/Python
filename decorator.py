# @Time: 2018/12/24-15:43
# @Author: wangyun

import time


def dec(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()
        proc_time = (end_time - start_time) * 1000
        print("1-100000数字相加的结果是%d运行的时间是%dms" % (ret, proc_time))

    return wrapper()


@dec
def test1():
    sum = 0
    for i in range(1, 100001):
        sum += i
    return sum


test1
