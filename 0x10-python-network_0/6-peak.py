#!/usr/bin/python3
"""It finds peak in unsorted list"""

def find_peak(list_of_integers):
    """unsorted list"""
    li = list_of_integers
    size = len(li)

    if size == 0:
        return None

    if size is 1:
        return li[0]

    return recurse(li, 0, size -1)

def recurse(li, left, right):
    """This is a recursive component"""
    m = int((left + right) / 2)

    if left > right:
        return li[m]

    if (m == 0 or li[m] > li[m - 1])\
       and (m == len(li) - 1 or li[m] > li[m + 1]):
        return li[m]

    elif (m > 0) and li[m - 1] > li[m]:
        return recurse(li, left, m - 1)
    else:
        return recurse(li, m + 1, right)
