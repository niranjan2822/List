# Merge two lists alternatively
# Given two lists, write a Python program to merge the given lists in an alternative fashion,
# provided that the two lists are of equal length.

'''
Examples:

Input : lst1 = [1, 2, 3]
        lst2 = ['a', 'b', 'c']
Output : [1, 'a', 2, 'b', 3, 'c']

Input : lst1 = ['name', 'alice', 'bob']
        lst2 = ['marks', 87, 56]
Output : ['name', 'marks', 'alice', 87, 'bob', 56]
'''


# Method #1 : List comprehension

# Python3 program to merge two lists
# alternatively

def countList(lst1, lst2):
    return [sub[item] for item in range(len(lst2))
            for sub in [lst1, lst2]]


# Driver code
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
print(countList(lst1, lst2))


# output : [1, 'a', 2, 'b', 3, 'c']

# There is an alternative to use list comprehension with zip() as given below –
def countList(lst1, lst2):
    return [item for pair in zip(lst1, lst2 + [0])
            for item in pair]


# Method #3 : Using reduce()

# Python3 program to merge two lists
# alternatively
import operator
from functools import reduce


def countList(lst1, lst2):
    return reduce(operator.add, zip(lst1, lst2))


# Driver code
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
print(countList(lst1, lst2))

# Method #4 : Using numpy module
# Python3 program to merge two lists
# alternatively
import numpy as np


def countList(lst1, lst2):
    return np.array([[i, j] for i, j in zip(lst1, lst2)]).ravel()


# Driver code
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
print(countList(lst1, lst2))



