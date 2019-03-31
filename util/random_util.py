# encoding: utf-8
'''
@file: random_util.py
@time: 2019/3/16 16:12
@desc:
'''

import random


def get_random_list(size=10):
    return get_random_list(size=size, offset=0, n=size * 10)


def get_random_list2(size=10):
    return get_random_list(size=size, offset=0, n=size)


def get_random_list(size=10, offset=0, n=1000):
    ret = []
    for i in range(size):
        r = int(random.random() * n + offset)
        ret.append(r)
    return ret


def get_sorted_list(size=10):
    ret = get_random_list(size)
    ret.sort()
    return ret


if __name__ == '__main__':
    list = get_random_list2(10)
    # list.sort()
    print(list)
