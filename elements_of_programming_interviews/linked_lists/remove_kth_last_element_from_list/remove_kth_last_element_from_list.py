# O(n) time | O(1) space
# Assumes L has at least k nodes, deletes k-th last node in L
def remove_kth_last_element_from_list(L, k):
    tmp = ListNode(0, L)
    first = tmp.next
    for _ in range(k):
        first = tmp.next
    second = tmp
    while tmp:
        first, second = first.next, second.next
    # second points to the (k+1)-th last node, deletes its successor
    second.next = second.next.next
    return tmp.next
