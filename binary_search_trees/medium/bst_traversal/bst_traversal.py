# O(N) time | O(N) space
def in_order_traversal(tree, array):
    if tree is not None:
        in_order_traversal(tree.left, array)
        array.append(tree.value)
        in_order_traversal(tree.right, array)
    return array
        
# O(N) time | O(N) space
def pre_order_traversal(tree, array):
    if tree is not None:
        array.append(tree.value)
        pre_order_traversal(tree.left, array)
        pre_order_traversal(tree.right, array)
    return array
        
# O(N) time | O(N) space
def post_order_traversal(tree, array):
    if tree is not None:
        post_order_traversal(tree.left, array)
        post_order_traversal(tree.right, array)
        array.append(tree.value)
    return array
        
