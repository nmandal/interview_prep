# O(n) time | O(1) space
def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        # Need additional digit as the most significant digit 
        # (i.e., A[0]) has a carry-out.
        A[0] = 0
        A.insert(0, 1)
    return A
        
