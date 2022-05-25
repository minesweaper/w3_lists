# Write a Python program to remove duplicates from a list.

a = [10,20,30,20,10,50,60,40,80,50,40]


def remove_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list


print(remove_duplicates(a))
            