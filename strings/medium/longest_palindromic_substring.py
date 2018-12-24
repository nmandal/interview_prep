#
def longest_palindromic_substring(string):
    curr_longest = [0,1]
    for i in range(1, len(string)):
        odd = get_longest_palindrome_from(string, i-1, i+1)
        even = get_longest_palindrome_from(string, i-1, i)
        longest = max(odd, even, key = lambda x: x[1] - x[0])
        curr_longest = max(curr_longest, longest, key = lambda x: x[1] - x[0])
    return curr_longest[]

def get_longest_palindrome_from(string, left, right):
    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1
    return [left+1, right]
