# O(N) time | O(1) space
def remove_kth_node_from_end(head, k):
    first = head
    second = head
    for i in range(k):
        first = first.next
    if first is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while first.next is not None:
        first = first.next
        second = second.next
    second.next = second.next.next
    return head
