# Union of two or more Lists
# Union of a list means, we must take all the elements from list A and list B (there can be more than two lists) and
# put them inside a single new list. There are various orders in which we can combine the lists. For e.g.,
# we can maintain the repetition and order or remove the repeated elements in the final list and so on.

'''
Examples : Maintained repetition only
Input :
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
Output :
[23, 15, 2, 14, 14, 16, 20, 52, 2, 48,
15, 12, 26, 32, 47, 54]

Maintained repetition and order
Input :
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
Output :
[2, 2, 12, 14, 14, 15, 15, 16, 20, 23,
26, 32, 47, 48, 52, 54]

Without repetition
Input :
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
Output :
[32, 2, 12, 14, 15, 16, 48, 47, 20, 52, 54, 23, 26]

Union of three lists
Input :
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
lst3 = [4, 78, 5, 6, 9, 25, 64, 32, 59]
Output :
[32, 64, 2, 4, 5, 6, 9, 12, 14, 15, 16,
48, 47, 78, 20, 52, 54, 23, 25, 26, 59]
'''


# Maintaining Repetition
#
# We can simply use the plus “+” operator inorder to combine two list into one. This will reflect the repetition.

# Python program to illustrate union
# Maintained repetition
def Union(lst1, lst2):
    final_list = lst1 + lst2
    return final_list


# Driver Code
lst1 = [23, 15, 2, 14, 14, 16, 20, 52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print(Union(lst1, lst2))


# output : [23, 15, 2, 14, 14, 16, 20, 52, 2, 48, 15, 12, 26, 32, 47, 54]

# Maintaining both Repetition and Order
# To maintain the order of appearance in the new list we need to use the sorted() function, passing the addition of two
# lists(plus operated, as in the previous problem) as parameters.

# Python program to illustrate union
# Maintained repetition and order
def Union(lst1, lst2):
    final_list = sorted(lst1 + lst2)
    return final_list


# Driver Code
lst1 = [23, 15, 2, 14, 14, 16, 20, 52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print(Union(lst1, lst2))


# output : [2, 2, 12, 14, 14, 15, 15, 16, 20, 23, 26, 32, 47, 48, 52, 54]

# Without Repetition
# To get rid of all the repetitive elements from the initial list, we use the set() function on both the lists,
# individually. Then we add them using the “+” operator and pass as a new list.

# Python program to illustrate union
# Without repetition
def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list


# Driver Code
lst1 = [23, 15, 2, 14, 14, 16, 20, 52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print(Union(lst1, lst2))


# output : [32, 2, 12, 14, 15, 16, 48, 47, 20, 52, 54, 23, 26]

# More than two lists
# We can also make an union of more than two lists. This can be done efficiently by using both the set() and union()
# function, simultaneously, as shown in the below example. This also takes care of the repetition and prevents them.

# Python program to illustrate union
# Union of three lists
# Python program to illustrate union
# Union of three lists
def Union(lst1, lst2, lst3):
	final_list = list(set().union(lst1, lst2, lst3))
	return final_list

# Driver Code
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
lst3 = [4, 78, 5, 6, 9, 25, 64, 32, 59]
print(Union(lst1, lst2, lst3))


# output : [2, 4, 5, 6, 9, 12, 14, 15, 16, 20, 23, 25, 26, 32, 47, 48, 52, 54, 59, 64, 78]

