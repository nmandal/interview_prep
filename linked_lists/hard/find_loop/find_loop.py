# O(n) time | O(1) space
def find_loop(head):
    slow = head.next
    fast = head.next.next
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
