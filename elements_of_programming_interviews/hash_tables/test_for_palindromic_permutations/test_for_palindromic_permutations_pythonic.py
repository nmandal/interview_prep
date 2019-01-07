# O(n) time | O(c) space where c is the number of distinct characters in the string
def can_string_be_palindrome(s):
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1
