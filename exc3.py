# Write a Python program to get the largest number from a list


def max_num_in_list(list):
    list.sort()
    max_num = list[-1]
    return max_num


print(max_num_in_list([1, 2, -8, 0]))