
def three_sum(A, t):
    def has_two_sum(array, target):
        i, j = 0, len(array) - 1
        while i <= j:
            if array[i] + array[j] == target:
                return True
            elif array[i] + array[j] < target:
                i += 1
            else:
                j -= 1
        return False

    A.sort()
    # Find if the sum of two numbers in A equals to t-a
    return any(has_two_sum(A, t-a) for a in A)
