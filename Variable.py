# variable is a container for a value (string, integer, float, boolean)
"""
And by the way in this way we can write multiple line comments
A variable behaves as if it was the value it creates
"""

# python catches small spacing errors remember even if I didn't gave space after the hash it showed error
# also we need space between equal to symbol and words

# STRINGS
first_name = 'Ganapati'
first_name ='champs'
print(f"Hello {first_name}")

""" here f is the f string formatted string written as f or F before the quotation marks 
In this string you can write a python expression between { and } characters that refers to variables/literal values """

# INTEGERS
age = 18
print(f'I am {age} years old.')

# FLOAT

bill = 67.45
print(f'the bill is of', bill, '₹')
# this is without the use of f string using commas(with appropriate white spaces)

# BOOLEAN
loves_python = True
if loves_python:
    print('I love you')
else:
    print("get lost")

    # tip: do the formatting until the {} gets highlighted in pycharm
    # ohh they also show spelling mistakes in comments 😮


