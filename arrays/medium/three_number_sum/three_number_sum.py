# O(N^2) time | O(N) space
def three_number_sum(array, target):
    triplet_sums = []
    array.sort()
    
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == target:
                triplet_sums.append(sorted((array[i], array[left], array[right])))
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return triplet_sums
