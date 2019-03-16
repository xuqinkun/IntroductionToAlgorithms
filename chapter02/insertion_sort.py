# -*- coding:utf-8 -*-

# 插入排序

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

if __name__ == '__main__':
    a = [6, 4, 2, 1, 8, 7, 10]
    insertion_sort(a)
    print(a)