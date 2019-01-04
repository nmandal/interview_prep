# O(nk) time | O(nk) space
def max_profit_with_k_transactions(prices, k):
    if not len(prices):
        return 0
    profits = [[0 for d in prices] for t in range(k+1)]
    for t in range(1, k+1):
        max_sofar = float('-inf')
        for d in range(1, len(prices)):
            max_sofar = max(max_sofar, profits[t-1][d-1] - prices[d-1])
            profits[t][d] = max(profits[t][d-1], max_sofar + prices[d])
    return profits[-1][-1]
