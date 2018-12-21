# BST Rule: its value is strictly greater than the
#           values of every node to its left; its value
#           is less than or equal to the values of 
#           every node to its right
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log N) time | O(log N) space
    # Worst: O(N) time | O(N) space
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self
    
    # Average: O(log N) time | O(log N) space
    # Worst: O(N) time | O(N) space
    def contains(self, value):
        if self.value == value:
            return True
        elif value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
    
    # Average: O(log N) time | O(log N) space
    # Worst: O(N) time | O(N) space
    def remove(self, value, parent=None):
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.get_min_value()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    self.value = None
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right = self.left if self.left is not None else self.right
        return self
