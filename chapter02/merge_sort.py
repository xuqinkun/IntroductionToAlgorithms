# -*- encoding: utf-8 -*-

'''
@Author  :   {YourName}
@File    :   selection_sort.py
@Time    :   2019/3/16 11:35
@Desc    :
'''
import sys
import math
from util import random_util

def merge(A=[], p=0, q=0, r=0):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(0, n1):
        L.append(A[p + i])
    for j in range(0, n2):
        R.append(A[q + j + 1])
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    j = 0
    k = 0
    for m in range(p, r + 1):
        if L[j] <= R[k]:
            A[m] = L[j]
            j += 1
        else:
            A[m] = R[k]
            k += 1
    pass

def merge_sort(A=[], p=0, r=0):
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

if __name__ == '__main__':
    # test merge
    # list1 = random_util.get_sorted_list()
    # list2 = random_util.get_sorted_list()
    # q = len(list1) - 1
    # print("list1:\n%s" % list1)
    # print("list2:\n%s" % list2)
    # list1 = list1 + list2
    # print("append:\n%s" % list1)
    # r = len(list1) - 1
    # merge(list1, 0, q, r)
    # print("merged:\n%s" % list1)

    # test merge_sort
    list = random_util.get_random_list(10)
    merge_sort(list, 0, len(list) - 1)
    print(list)