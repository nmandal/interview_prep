# O(nc) time | O(nc) space
def knapsack_problem(items, capacity):
    knapsack_values = [[0 for x in range(0, capacity+1)] for y in range(0, len(items) + 1)]
    for i in range(1, len(items) + 1):
        curr_weight = items[i-1][1]
        curr_value = items[i-1][0]
        for c in range(0, capacity+1):
            if curr_weight > c:
                knapsack_values[i][c] = knapsack_values[i-1][c]
            else:
                knapsack_values[i][c] = max(knapsack_values[i-1][c], knapsack_values[i-1][c-curr_weight] + curr_value)
    return [knapsack_values[-1][-1], build_knapsack(knapsack_values, items)]

def build_knapsack(knapsack_values, items):
    seq = []
    i = len(knapsack_values) - 1
    c = len(knapsack_values[0]) - 1
    while i > 0:
        if knapsack_values[i][c] == knapsack_values[i-1][c]:
            i -= 1
        else:
            seq.append(i-1)
            c -= items[i-1][1]
            i -= 1
        if c == 0:
            break
    return list(reversed(seq)})
