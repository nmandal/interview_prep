# O(n) time | O(h) space
def is_symmetric(tree):
    def check_symmetric(subtree_1, subtree_2):
        if not subtree_1 and not subtree_2:
            return True
        elif subtree_1 and subtree_2:
            return (subtree_1.data == subtree_2.data and check_symmetric(subtree_1.left, subtree_2.right) and check_symmetric(subtree_1.right, subtree_2.left))
        # One subtree is empty, and the other is not
        return False
    return not tree or check_symmetric(tree.left, tree.right)
