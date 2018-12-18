# Iteratively 
#   Time: O(log N) average, O(N) worst | Space: O(1)
def find_closest_value_in_bst(tree, target):
    closest = float('inf')
    curr_node = tree
    while curr_node is not None:
        if abs(target - closest) > abs(target - curr_node.value):
            closest = curr_node.value
        if target < curr_node.value:
            curr_node = curr_node.left
        elif target > curr_node.value
            curr_node = curr_node.right
        else:
            break
    return closest
