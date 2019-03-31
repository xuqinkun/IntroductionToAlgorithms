# encoding: utf-8
'''
@file: count_reverse_order.py
@time: 2019/3/17 13:53
@desc: 假设A是一个有n个不同数的数组，若i<j且A[i]>A[j]，则对偶(i, j)称为A的一个逆序对
       给出一个确定在n个元素的任何排列中逆序对数量的算法，最坏情况需要O(nlgn)时间
'''

import sys
from util import random_util

"""
    merge时，如果提取R数组中的元素，则L中剩余多少个元素，此时就有多少逆序数
"""
def merge(A=[], p=0, q=0, r=0):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(0, n1):
        L.append(A[p + i])
    for i in range(0, n2):
        R.append(A[q + i + 1])
    L.append(sys.maxsize)
    R.append(sys.maxsize)

    j = 0
    k = 0
    reverse_count = 0
    for i in range(p, r + 1):
        if L[j] < R[k]:
            A[i] = L[j]
            j += 1
        else:
            A[i] = R[k]
            k += 1
            reverse_count += n1 - j
    return reverse_count


def count_reverse(A=[], p=0, q=0):
    inversions = 0
    if p < q:
        mid = int((p + q) / 2)
        inversions += count_reverse(A, p, mid)
        inversions += count_reverse(A, mid + 1, q)
        inversions += merge(A=A, p=p, q=mid, r=q)
    return inversions


if __name__ == '__main__':
    list = random_util.get_random_list(5)
    print("src:%s" % list)
    cnt = count_reverse(list, 0, len(list) - 1)
    print("sorted:%s" % list)
    print("reverse number: %s " % cnt)