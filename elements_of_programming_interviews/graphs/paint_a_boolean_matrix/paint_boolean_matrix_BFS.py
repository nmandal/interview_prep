# O(mn) time | O(m+n) space
def flip_color(x, y, A):
    Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))
    color = A[x][y]
    q = collections.dequeue([Coordinate(x, y)])
    A[x][y] = 1 - A[x][y] # Flips
    while q:
        x, y = q.popleft()
        for d in (0,1), (0,-1), (1,0), (-1,0):
            next_x, next_y = d[0], d[1]
            if (0 <= next_x < len(A) and 0 <= next_y < len(A[next_x])) and A[next_x][next_y] == color:
                # Flip the color
                A[next_x][next_y] = 1 - A[next_x][next_y]
                q.append(Coordinate(next_x, next_y))
