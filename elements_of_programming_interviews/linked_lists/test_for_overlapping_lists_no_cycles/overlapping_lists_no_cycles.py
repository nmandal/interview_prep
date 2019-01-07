# O(n) time | O(1) space
def overlapping_no_cycle_lists(L1, L2):
    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length
    L1_len, L2_len = length(L1), length(L2)
    if L1_len > L2_len:
        L1, L2 = L2, L1 # Make L2 the longer list
    # Advance longer list to get equal length lists
    for i in range(abs(L1_len - L2_len)):
        L2 = L2.next
        
    while L1 and L2 and L1 is not L2:
        L1, L2 = L1.next, L2.next
    return L1 # None implies there is no overlap between L1 and L2
