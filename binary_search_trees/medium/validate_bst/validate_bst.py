# O(N) time | O(d) space
def validate_bst(tree):
    return _validate_bst(tree, float('-inf'), float('inf'))

def _validate_bst(tree, minimum, maximum):
    if tree is None:
        return True
    if tree.value < minimum or tree.value >= maximum:
        return False
    return _validate_bst(tree.left, minimum, tree.value) and _validate_bst(tree.right, tree.value, maximum)
