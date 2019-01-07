# O(nd) time | O(n) space
def min_number_of_coins_for_change(n, denoms):
    num_of_coins = [float('inf') for amount in range(n+1)]
    num_of_coins[0] = 0
    for denom in denoms:
        for amount in range(len(num_of_coins)):
            if denom <= amount:
                num_of_coins[amount] = min(num_of_coins[amount], 1 + num_of_coins[amount-denom])
            return num_of_coins[n] if num_of_coins[n] != float('inf') else -1
