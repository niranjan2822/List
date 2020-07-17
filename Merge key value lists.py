# Merge key value lists

'''

Input 1 : [0, 0, 0, 1, 1, 1, 2, 2]
Input 2  : [‘gfg’, ‘is’, ‘best’, ‘Akash’, ‘Akshat’, ‘Nikhil’, ‘apple’, ‘grapes’]
Output  : {0: [‘gfg’, ‘is’, ‘best’], 1: [‘Akash’, ‘Akshat’, ‘Nikhil’], 2: [‘apple’, ‘grapes’]}
'''

# Method #1 : Using zip() + loop + defaultdict()

# The combination of above method can be used to perform this particular task.
# In this, we use zip function to match the like elements of lists with each other and loop is then used to assign the
# keys with value from zipped list to add value to a defaultdict.

# Python3 code to demonstrate working of
# Merge key value list
# Using zip() + loop + defaultdict()
from collections import defaultdict

# initializing lists
test_list1 = [0, 0, 0, 1, 1, 1, 2, 2]
test_list2 = ['gfg', 'is', 'best', 'Akash', 'Akshat', 'Nikhil', 'apple', 'grapes']

# printing original lists
print("The original list1 is : " + str(test_list1))
print("The original list2 is : " + str(test_list2))

# Using zip() + loop + defaultdict()
# Merge key value list
res = defaultdict(list)
for i, j in zip(test_list1, test_list2):
    res[i].append(j)

# printing result
print("The merged key value dictionary is : " + str(dict(res)))

# output : The original list1 is : [0, 0, 0, 1, 1, 1, 2, 2]
# The original list2 is : ['gfg', 'is', 'best', 'Akash', 'Akshat', 'Nikhil', 'apple', 'grapes']
# The merged key value dictionary is : {0: ['gfg', 'is', 'best'], 1: ['Akash', 'Akshat', 'Nikhil'], 2: ['apple', 'grapes']}

