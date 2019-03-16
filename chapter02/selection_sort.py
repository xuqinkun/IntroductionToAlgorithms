# -*- encoding: utf-8 -*-

'''
@Author  :   {YourName}

@File    :   selection_sort.py

@Time    :   2019/3/16 11:35

@Desc    :

'''

"""
   首先找出A中的最小元素与A[0]交换，接着，
   找出A中次小的元素与A[1]交换，对A中前n-1个元素继续执行该操作。
"""
def selection_sort(A=[]):
    for i in range(0, len(A) - 2):
        index = i
        min = A[i]
        j = i
        while j < len(A):
            if A[j] < min:
                min = A[j]
                index = j
            j += 1
        tmp = A[i]
        A[i] = A[index]
        A[index] = tmp

if __name__ == '__main__':
    A = [5, 4, 3, 2, 1]
    selection_sort(A)
    print(A)



