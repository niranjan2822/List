# Zipping two lists of lists
'''

The original list 1 is : [[1, 3], [4, 5], [5, 6]]
The original list 2 is : [[7, 9], [3, 2], [3, 10]]
The modified zipped list is : [[1, 3, 7, 9], [4, 5, 3, 2], [5, 6, 3, 10]]
'''
#The normal zip function allows us the functionality to aggregate the values in a container.
# But sometimes, we have a requirement in which we require to have multiple lists and containing lists as index elements and
# we need to merge/zip them together

# Method #1 : Using map() + __add__

# This problem can be solved using the map function with the addition operation.
# The map function performs the similar kind of function as the zip function and in this this case
# can help to reach to a solution.

# Python3 code to demonstrate
# zipping lists of lists
# using map() + __add__

# initializing lists
test_list1 = [[1, 3], [4, 5], [5, 6]]
test_list2 = [[7, 9], [3, 2], [3, 10]]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# using map() + __add__
# zipping lists of lists
res = list(map(list.__add__, test_list1, test_list2))

# printing result
print("The modified zipped list is : " + str(res))

# output : The original list 1 is : [[1, 3], [4, 5], [5, 6]]
# The original list 2 is : [[7, 9], [3, 2], [3, 10]]
# The modified zipped list is : [[1, 3, 7, 9], [4, 5, 3, 2], [5, 6, 3, 10]]

# Method #2 : Using itertools.chain() + zip()

#This combination of these two functions can be used to perform this particular task.
# The chain function can be used to perform the interlist aggregation, and the intralist aggregation
# is done by zip function.

# Python3 code to demonstrate
# zipping lists of lists
# using map() + __add__
import itertools

# initializing lists
test_list1 = [[1, 3], [4, 5], [5, 6]]
test_list2 = [[7, 9], [3, 2], [3, 10]]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# using map() + __add__
# zipping lists of lists
res = [list(itertools.chain(*i))
       for i in zip(test_list1, test_list2)]

# printing result
print("The modified zipped list is : " + str(res))


