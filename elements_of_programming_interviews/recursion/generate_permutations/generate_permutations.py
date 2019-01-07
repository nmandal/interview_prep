# O(n*n!) time | O(n*n!) space
def generate_permutations(A):
    def directed_permutations(i):
        if i == len(A) - 1:
            result.append(A.copy)
            return
        
        # Try every possibility for A[j]
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            directed_permutations(i+1)
            A[i], A[j] = A[j], A[i]
            
    result = []
    directed_permutations(0)
    return result
