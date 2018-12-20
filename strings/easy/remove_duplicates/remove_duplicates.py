import timeit

def remove_duplicates(array):
    chars = {}
    for char in array:
        if char in chars:
            array.pop(char)
        else:
            chars[char] = char
    return array

def alt_remove_duplicates(array):
    return set(array)

print(timeit.timeit(remove_duplicates[1,3,2,5,6,3,3,1,1,2,5,7]))
print(timeit.timeit(alt_remove_duplicates[1,3,2,5,6,3,3,1,1,2,5,7]))
