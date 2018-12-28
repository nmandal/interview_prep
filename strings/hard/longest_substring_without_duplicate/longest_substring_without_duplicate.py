# O(n) time | O(min(n, a)) space
def longest_substring_without_duplicate(string):
    last_seen = {}
    longest = []
    start = 0
    for i, char in enumerate(string):
        if char in last_seen:
            start = max(start, last_seen[char] + 1)
        if longest[1] - longest[0] < i + 1 - start:
            longest = [start, i+1]
        last_seen[char] = i
    return string[longest[0]:longest[1]]
