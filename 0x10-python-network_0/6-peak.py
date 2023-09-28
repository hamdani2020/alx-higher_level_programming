#!/usr/bin/python3
"""It finds peak in list of unsorted integers
"""


def find_peak(list_of_integers):
    """It fiinds peak in unsorted list
    """
    li = list_of_integers
    s = len(li)

    if s == 0:
        return None

    if s is 1:
        return li[0]

    return recurse(li, 0, s - 1)


def recurse(li, left, right):
    """A Recursive component
    """
    m = int((left + right) / 2)

    if left > right:
        return li[m]

    if (m == 0 or li[m] > li[m - 1])\
       and (m == len(li) - 1 or li[m] > li[m + 1]):
        return li[m]

    # recurse left
    elif (m > 0) and li[m - 1] > li[m]:
        return recurse(li, left, m - 1)
    else:  # recurse right
        return recurse(li, m + 1, right)
