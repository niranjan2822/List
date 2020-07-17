# Average of two lists


'''

The original list 1 is : [1, 3, 4, 5, 2, 6]
The original list 2 is : [3, 4, 8, 3, 10, 1]
The Average of both lists is : 4.166666666666667

'''

# Method #1 : Using sum() + len() + “+” operator
# The average value can be determined by the conventional sum() and len function of python and the extension of
# one to two lists can be dealt using the “+” operator.

# Python3 code to demonstrate
# Average of two lists
# using sum() + len() + "+" operator

# initializing lists
test_list1 = [1, 3, 4, 5, 2, 6]
test_list2 = [3, 4, 8, 3, 10, 1]

# printing the original lists
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))

# Average of two lists
# using sum() + len() + "+" operator
res = sum(test_list1 + test_list2) / len(test_list1 + test_list2)

# printing result
print ("The Average of both lists is : " + str(res))

# output : The original list 1 is : [1, 3, 4, 5, 2, 6]
# The original list 2 is : [3, 4, 8, 3, 10, 1]
# The Average of both lists is : 4.166666666666667

# Method #2 : Using sum() + len() + chain()

# Python3 code to demonstrate
# Average of two lists
# using sum() + len() + "+" operator
from itertools import chain

# initializing lists
test_list1 = [1, 3, 4, 5, 2, 6]
test_list2 = [3, 4, 8, 3, 10, 1]

# printing the original lists
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))

# Average of two lists
# using sum() + len() + "+" operator
res = sum(chain(test_list1, test_list2)) / len(list(chain(test_list1, test_list2)))

# printing result
print ("The Average of both lists is : " + str(res))

