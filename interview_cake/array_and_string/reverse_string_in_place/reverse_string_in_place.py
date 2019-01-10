# O(n) time | O(1) space
def reverse_in_place(string):
    s = list(string)
    left = 0
    right = len(s) - 1
    for _ in range(len(s) // 2):
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return str(s)
