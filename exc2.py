# Write a Python program to multiply all the items in a list.

list = [2,2,-8]


def multiply_in_list(list):
    result = 1
    for i in list:
        result *= i
    return result


print(multiply_in_list(list))