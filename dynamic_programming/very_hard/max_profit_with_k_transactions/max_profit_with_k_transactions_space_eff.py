# O(nk) time | O(n) space
def max_profit_with_k_transactions(prices, k):
    if not len(prices):
        return 0
    even_profits = [0 for d in prices]
    odd_profits = [0 for d in prices]
    for t in range(1, k+1):
        max_sofar = float('-inf')
        if t % 2 == 1:
            curr_profits = odd_profits
            prev_profits = even_profits
        else:
            curr_profits = even_profits
            prev_profits= odd_profits
        for d in range(1, len(prices)):
            max_sofar = max(max_sofar, prev_profits[d-1] - prices[d-1])
            curr_profits[d] = max(curr_profits[d-1], max_sofar + prices[d])
    return even_profits[-1] if k % 2 == 0 else odd_profits[-1]
