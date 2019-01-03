# O(n) time | O(n) space
def reverse_digtis(num):
    result, num_remaining = 0, abs(num_remaining)
    while num_remaining:
        result = result * 10 + num_remaining % 10
        num_remaining //= 10
    return -result if num < 0 else num
