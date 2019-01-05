# O(n^3) time | O(n^2) space
def palindrome_partitioning_min_cuts(string):
    palindromes = [[False for i in string] for j in string]
    for i in range(len(string)):
        for j in range(len(string)):
            palindromes[i][j] = is_palindrome(string[i:j+1])
    cuts = [float('inf') for i in string]
    for i in range(len(string)):
        if palindromes[0][i]:
            cuts[i] = 0
        else:
            cuts[i] = cuts[i-1] + 1
            for j in range(1, i):
                if palindromes[j][i] and cuts[j-1] + 1 < cuts[i]:
                    cuts[i] = cuts[j-1] + 1
    return cuts[-1]

def is_palindrome(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True
