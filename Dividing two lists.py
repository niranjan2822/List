# Dividing two lists

'''
Input 1 -->  list 1 is : [3, 5, 2, 6, 4]
Input 2 -->  list 2 is : [7, 3, 4, 1, 5]
Output  : [0.42857142857142855, 1.6666666666666667, 0.5, 6.0, 0.8]

'''

# Method #1 : Using zip() + list comprehension

# The zip operation can be used to link one list with the other and the computation part can be handled by the list
# comprehension and hence providing a shorthand to this particular problem.

# Python3 code to demonstrate
# division of lists
# using zip() + list comprehension

# initializing lists
test_list1 = [3, 5, 2, 6, 4]
test_list2 = [7, 3, 4, 1, 5]

# printing original lists
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))

# division of lists
# using zip() + list comprehension
res = [i / j for i, j in zip(test_list1, test_list2)]

# printing result
print ("The division list is : " + str(res))

# Output : The original list 1 is : [3, 5, 2, 6, 4]
# The original list 2 is : [7, 3, 4, 1, 5]
# The division list is : [0.42857142857142855, 1.6666666666666667, 0.5, 6.0, 0.8]

# Method #2 : Using map()

# Using map function is most elegant way in which we can possibly perform the twining of a function with both the lists.
# Different operations other than division can also be applied over it.

# Python3 code to demonstrate
# division of lists
# using map()
from operator import truediv

# initializing lists
test_list1 = [3, 5, 2, 6, 4]
test_list2 = [7, 3, 4, 1, 5]

# printing original lists
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))

# division of lists
# using map()
res = list(map(truediv, test_list1, test_list2))

# printing result
print ("The division list is : " + str(res))
