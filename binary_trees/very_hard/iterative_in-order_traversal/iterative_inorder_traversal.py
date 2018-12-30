# O(n) time | O(1) space
def iterative_inorder_traversal(tree, callback):
    prev = None
    curr = tree
    while curr is not None:
        if prev is None or prev == curr.parent:
            if curr.left is not None:
                nex = curr.left
            else:
                callback(curr)
                nex = curr.right if curr.right is not None else curr.parent
        elif prev == curr.left:
            callback(curr)
            nex = curr.right if curr.right is not None else curr.parent
        else:
            nex = curr.parent
        prev = curr
        curr = nex
