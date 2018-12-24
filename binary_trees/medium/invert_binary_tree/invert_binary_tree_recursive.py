# O(N) time | O(D) space
def invert_binary_tree_recursive(tree):
    if tree is None:
        return
    swap_left_and_right(tree)
    invert_binary_tree_recursive(tree.left)
    invert_binary_tree_recursive(tree.right)

    
def swap_left_and_right(tree):
    tree.left, tree.right = tree.right, tree.left
