# Combining two sorted lists

'''
The original list 1 is : [1, 5, 6, 9, 11]
The original list 2 is : [3, 4, 7, 8, 10]
The combined sorted list is : [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]

'''

# Method #1 : Naive Method

# Python3 code to demonstrate
# to combine two sorted list
# using naive method

# initializing lists
test_list1 = [1, 5, 6, 9, 11]
test_list2 = [3, 4, 7, 8, 10]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# using naive method
# to combine two sorted lists
size_1 = len(test_list1)
size_2 = len(test_list2)

res = []
i, j = 0, 0

while i < size_1 and j < size_2:
    if test_list1[i] < test_list2[j]:
        res.append(test_list1[i])
        i += 1

    else:
        res.append(test_list2[j])
        j += 1

res = res + test_list1[i:] + test_list2[j:]

# printing result
print("The combined sorted list is : " + str(res))

# output : The original list 1 is : [1, 5, 6, 9, 11]
# The original list 2 is : [3, 4, 7, 8, 10]
# The combined sorted list is : [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Method #2 : Using sorted()
# Python3 code to demonstrate
# to combine two sorted list
# using sorted()

# initializing lists
test_list1 = [1, 5, 6, 9, 11]
test_list2 = [3, 4, 7, 8, 10]

# printing original lists
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))

# using sorted()
# to combine two sorted lists
res = sorted(test_list1 + test_list2)

# printing result
print ("The combined sorted list is : " + str(res))
