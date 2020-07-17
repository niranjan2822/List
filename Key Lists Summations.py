# Key Lists Summations
# Sometimes, while working with Python Dictionaries, we can have problem in which we need to perform the replace of
# key with values with sum of all keys in values

'''

Input : {‘gfg’: [4, 6, 8], ‘is’: [9, 8, 2], ‘best’: [10, 3, 2]}
output : {‘gfg’: 18, ‘is’: 19, ‘best’: 15}

'''

# Method #1 : Using sum() + loop

# This is one of the ways in which this task can be performed. In this, we perform the summation using sum, and
# iteration to each key is done in brute way using loop.

# Python3 code to demonstrate working of
# Key Values Summations
# Using sum() + loop

# initializing dictionary
test_dict = {'gfg': [4, 6, 8], 'is': [9, 8, 2], 'best': [10, 3, 2]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Key Values Summations
# Using sum() + loop
for key, value in test_dict.items():
    test_dict[key] = sum(value)

# printing result
print("The summation keys are : " + str(test_dict))

# output : The original dictionary is : {'gfg': [4, 6, 8], 'is': [9, 8, 2], 'best': [10, 3, 2]}
# The summation keys are : {'gfg': 18, 'is': 19, 'best': 15}