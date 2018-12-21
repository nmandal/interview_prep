# BST Rule: its value is strictly greater than the
#           values of every node to its left; its value
#           is less than or equal to the values of 
#           every node to its right
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log N) time | O(1) space
    # Worst: O(N) time | O(1) space
    def insert(self, value):
        curr = self
        while True:
            if value < curr.value:
                if curr.left is None:
                    curr.left = BST(value)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BST(value)
                    break
                else:
                    curr = curr.right
        return self
    
    # Average: O(log N) time | O(1) space
    # Worst: O(N) time | O(1) space
    def contains(self, value):
        curr = self
        while curr is not None:
            if value < curr.value:
                curr = curr.left
            elif value > curr.value:
                curr = curr.right
            else:
                return True
        return False
    
    # Average: O(log N) time | O(1) space
    # Worst: O(N) time | O(1) space
    def remove(self, value, parent=None):
        curr = self
        while curr is not None:
            if value < curr.value:
                parent_node = curr
                curr = curr.left
            elif value > curr.value:
                parent_node = curr
                curr = curr.right
            else:
                if curr.left is not None and curr.right is not None:
                    curr.value = curr.right.get_min_value()
                    curr.right.remove(curr.value, curr)
                elif parent_node is None:
                    if curr.left is not None:
                        curr.value = curr.left.value
                        curr.right = curr.left.right
                        curr.left = curr.left.left
                    elif curr.right is not None:
                        curr.value = curr.right.value
                        curr.left = curr.right.left
                        curr.right = curr.right.right
                    else:
                        curr.value = None
                elif parent_node.left == curr:
                    parent_node.left = curr.left if curr.left is not None else curr.right
                elif parent_node.right == curr:
                    parent_node.right = curr.left if curr.left is not None else curr.right
                break
            return self
                    
    def get_min_value(self):
        curr = self
        while curr.left is not None:
            curr = curr.left
        return curr.value
