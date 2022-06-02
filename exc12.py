# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']


def remove_from_list(my_list):
    my_list.pop(5)
    my_list.pop(4)
    my_list.pop(0)
    return my_list


sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(remove_from_list(sample_list))


# Second solution
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i, x) in enumerate(color) if i not in (0, 4, 5)]
print(color)


