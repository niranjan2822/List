# Iterating two lists at once

# Sometimes, while working with Python list, we can have a problem in which we have to iterate over two list elements.
# Iterating one after another is an option, but it’s more cumbersome and a one-two liner is always recommended over
# that

'''

Input 1  : [4, 5, 3, 6, 2]
Input 2 : [7, 9, 10, 0]
The paired list contents are :
4 5 3 6 2 7 9 10 0

'''

# Method #1 : Using loop + “+” operator

# Python3 code to demonstrate working of
# Iterating two lists at once
# using loop + "+" operator

# initializing lists
test_list1 = [4, 5, 3, 6, 2]
test_list2 = [7, 9, 10, 0]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Iterating two lists at once
# using loop + "+" operator
# printing result
print("The paired list contents are : ")
for ele in test_list1 + test_list2:
    print(ele, end=" ")

# output : Output :
# The original list 1 is : [4, 5, 3, 6, 2]
# The original list 2 is : [7, 9, 10, 0]
# The paired list contents are :
# 4 5 3 6 2 7 9 10 0

# Method #2 : Using chain()

# This is the method similar to above one, but it’s slightly more memory efficient as the chain() is used to
# perform the task and creates an iterator internally.

# Python3 code to demonstrate working of
# Iterating two lists at once
# using chain()
from itertools import chain

# initializing lists
test_list1 = [4, 5, 3, 6, 2]
test_list2 = [7, 9, 10, 0]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Iterating two lists at once
# using chain()
# printing result
print("The paired list contents are : ")
for ele in chain(test_list1, test_list2):
    print(ele, end=" ")


