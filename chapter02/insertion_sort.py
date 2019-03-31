# -*- coding:utf-8 -*-

# 插入排序

from chapter02 import binary_search

def insertion_sort(a=[]):
    for i in range(1, len(a)):
        key = a[i]
        # insert key into a[0...i - 1]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    pass

"""
    使用二分查找反向扫描，找到A[j]的位置,
    移动数组代码O(n)时间复杂度
"""

def do_binary_search(A=[], l=0, r=0, target=0):
    while l <= r:
        mid = int((l + r) / 2)
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l

def insert_sort2(a=[]):
    for i in range(1, len(a)):
        key = a[i]
        # insert key into a[0...i - 1]
        binary_search.binary_search(a, 0, i - 1, target=key)
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    pass


if __name__ == '__main__':
    a = [6, 4, 2, 1, 8, 7, 10]
    insertion_sort(a)
    print(a)