# Write a Python program to generate and print a list of first and last 5 elements where
# the values are square of numbers between 1 and 30 (both included).

my_list = []
for x in range(1, 31):
    x = x**2
    my_list.append(x)

print(my_list[:5])
print(my_list[-5:])