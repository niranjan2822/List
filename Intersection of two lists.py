# Intersection of two lists
# Intersection of two list means we need to take all those elements which are common to both of the initial lists
# and store them into another list. Now there are various ways in Python, through which we can perform the Intersection
# of the lists.

'''

Input :
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
Output :
[9, 10, 4, 5]

Input :
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
Output :
[9, 11, 26, 28]
'''


# Approach 1 :

# Python program to illustrate the intersection
# of two lists in most simple way

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


# Driver Code
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(lst1, lst2))


# output : [9, 11, 26, 28]

# Method 2:
# This method includes the use of set() method.

# Python program to illustrate the intersection
# of two lists using set() method
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


# Driver Code
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
print(intersection(lst1, lst2))

# output : [9, 10, 4, 5]

# Method 3:
# In this method we set() the larger list and then use the built-in function called interscetion() to compute the
# intersected list. intersection() is a first-class part of set.

# Python program to illustrate the intersection
# of two lists using set() and intersection()
def Intersection(lst1, lst2):
    return set(lst1).intersection(lst2)


# Driver Code
lst1 = [4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
lst2 = [9, 9, 74, 21, 45, 11, 63]
print(Intersection(lst1, lst2))

# output : {9, 11}


