class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.add_left_to_stack(root)
        
    def has_next(self):
        return True if self.stack else False

    def next(self):
        curr = self.stack.pop()
        self.add_left_to_stack(curr.right)
        return curr.value
    
    def add_left_to_stack(self, node):
        while node is not None:
            self.stack.push(node)
            node = node.left
