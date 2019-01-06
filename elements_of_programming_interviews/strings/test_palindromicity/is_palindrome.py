# O(n) time | O(1) space
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while not s[left].isalnum() and left < right:
            left += 1
        while not s[right].isalnum() and left < right:
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left, right = left - 1, right - 1
    return True
