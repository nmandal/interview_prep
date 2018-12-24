# O(N) time | O(N) space
def invert_binary_tree(tree):
    queue = [tree]
    while(len(queue)):
        curr = queue.pop()
        if curr is None:
            continue
        swap_left_and_right(curr)
        queue.append(curr.left)
        queue.append(curr.right)

def swap_left_and_right(tree):
    tree.left, tree.right = tree.right, tree.left
