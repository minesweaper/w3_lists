# Write a Python program to find the list of words that are longer than n from a given list of words


def long_words(n, string):
    list_of_words = string.split(" ")
    long = []
    for i in list_of_words:
        if len(i) > n:
            long.append(i)
    return long

print(long_words(3, "The quick brown fox jumps over the lazy dog"))

