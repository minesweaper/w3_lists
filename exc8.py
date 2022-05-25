# Write a Python program to check a list is empty or not.

a = []
b = ['a', 'b', 'c']


def validate_empty(list):
    if not list:
        return print("List in empty")
    else:
        return print("List is not empty")


validate_empty(a)
validate_empty(b)
