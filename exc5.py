# Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings
# Sample List : ['abc', 'xyz', 'aba', '1221']


def count_strings(list):
    count = 0
    for x in list:
        if len(x) > 2 and x[0] == x[-1]:
            count += 1
    return count


sample = ['abc', 'xyz', 'aba', '1221']
print(count_strings(sample))