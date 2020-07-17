# Merge two list of lists according to first element

'''
Input : lst1 = [[1, 'Alice'], [2, 'Bob'], [3, 'Cara']]
        lst2 = [[1, 'Delhi'], [2, 'Mumbai'], [3, 'Chennai']]
Output : [[1, 'Alice', 'Delhi'], [2, 'Bob', 'Mumbai'], [3, 'Cara', 'Chennai']]

Input : lst1 = [ ['c', 'class'], ['g', 'greek'], ]
        lst2 = [['c', 'coder'], ['g', 'god'], ]
Output : [['c', 'class', 'coder'], ['g', 'greek', 'god']]
'''

# Method #1 : Python zip() with list comprehension

# Python3 program to Merge two list of
# lists according to first element

def merge(lst1, lst2):
    return [a + [b[1]] for (a, b) in zip(lst1, lst2)]


# Driver code
lst1 = [[1, 'Alice'], [2, 'Bob'], [3, 'Cara']]
lst2 = [[1, 'Delhi'], [2, 'Mumbai'], [3, 'Chennai']]
print(merge(lst1, lst2))

# output : [[1, 'Alice', 'Delhi'], [2, 'Bob', 'Mumbai'], [3, 'Cara', 'Chennai']]

# Method #2 : Python enumerate() with list comprehension

# Python3 program to Merge two list of
# lists according to first element
import collections


def merge(lst1, lst2):
    return [(sub + [lst2[i][-1]]) for i, sub in enumerate(lst1)]


# Driver code
lst1 = [[1, 'Alice'], [2, 'Bob'], [3, 'Cara']]
lst2 = [[1, 'Delhi'], [2, 'Mumbai'], [3, 'Chennai']]
print(merge(lst1, lst2))

