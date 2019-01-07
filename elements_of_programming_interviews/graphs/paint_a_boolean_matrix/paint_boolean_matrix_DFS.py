# O(mn) time | O(m+n) space
def flip_color(x, y, A):
    color = A[x][y]
    A[x][y] = 1 - A[x][y]
    for d in (0,1), (0,-1), (1,0), (-1,0):
        next_x, next_y = x+d[0], y+d[1]
        if (0 <= next_x < len(A) and 0 <= next_y < len(A[next_x]) and A[next_x][next_y] == color):
            flip_color(next_x, next_y, A)
    
