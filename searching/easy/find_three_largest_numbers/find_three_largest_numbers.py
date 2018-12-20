# O(N) time | O(1) space
def find_three_largest_numbers(array):
    three_largest = [float('-inf'),float('-inf'),float('-inf')]
    for num in array:
        update_largest(three_largest, num)
    return three_largest

def update_largest(three_largest, num):
        if num > three_largest[2]:
            shift_and_update(three_largest, num, 2)
        elif num > three_largest[1]:
            shift_and_update(three_largest, num, 1)
        elif num > three_largest[0]:
            shift_and_update(three_largest, num, 0)

def shift_and_update(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i+1]
