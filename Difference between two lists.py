# Difference between two lists
'''
         Input :
list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]
Output :
[10, 20, 30, 15]
Explanation:
resultant list = list1 - list2
'''


# By the use of set()

# In this method we convert the lists into sets explicitly and then simply reduce one from the other
# using the subtract operator.

# Python code t get difference of two lists
# Using set()

def Diff(li1, li2):
    return (list(set(li1) - set(li2)))


# Driver Code
li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35]
print(Diff(li1, li2))

#output :  [10, 20, 30, 15]

# Without using the set()

# In this method, we use the basic combination technique to copy elements from both the list with a regular check
# if one is present in the other or not.

# Python code t get difference of two lists
# Not using set()

def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif


# Driver Code
li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35]
li3 = Diff(li1, li2)
print(li3)


