# encoding: utf-8
'''
@file: binary_search.py
@time: 2019/3/16 20:50
@desc:
'''

from util import random_util

def binary_search(A=[], target=0):
    r = len(A) - 1
    return do_binary_search(A=A, l=0, r=r, target=target)

def do_binary_search(A=[], l=0, r=0, target=0):
    while l <= r:
        mid = int((l + r) / 2)
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    print("l=%s r=%s" % (l, r))
    return -1

if __name__ == '__main__':
    # list = random_util.get_sorted_list()
    list = [7, 35, 85, 184, 192, 210, 216, 361, 471, 872]
    target = 0
    print("src:%s\ntarget:%s" % (list, target))
    ret = binary_search(A=list, target=target)
    print(ret)
    # for i in range(0, len(list)):
    #     target = list[i]
    #     print("src:%s\ntarget:%s" % (list, target))
    #     ret = binary_search(A=list, target=target)
    #     print(ret)