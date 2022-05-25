# Write a Python program to get the smallest number from a list

def min_number_in_list(list):
    list.sort()
    min = list[0]
    return min


print(min_number_in_list([1, 2, -8, 0]))