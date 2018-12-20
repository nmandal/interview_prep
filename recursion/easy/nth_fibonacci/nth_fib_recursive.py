# O(2^N) time | O(N) space
def getNthFib(n):
    if n in [1,2]:
        return n-1
    return getNthFib(n-1) + getNthFib(n-2)
