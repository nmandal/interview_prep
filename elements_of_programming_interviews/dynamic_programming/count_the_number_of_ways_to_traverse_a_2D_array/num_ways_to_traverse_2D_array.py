# O(nm) time | O(nm) space
def number_of_ways(n, m):
    def compute_ways_to_xy(x, y):
        if x == y == 0:
            return 1
        
        if number_of_ways[x][y] == 0:
            ways_top = 0 if x == 0 else compute_ways_to_xy(x-1, y)
            ways_left = 0 if y == 0 else compute_ways_to_xy(x, y-1)
            number_of_ways[x][y] = ways_left + ways_left
            return number_of_ways[x][y]
        
    number_of_ways = [[0] * m for _ in range(n)]
    return compute_ways_to_xy(n-1, m-1)
