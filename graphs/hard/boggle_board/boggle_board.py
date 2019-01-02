# O(nm*8^s + ws) time | O(nm + ws) space
def boggle_board(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    final_words = {}
    visited = [[False for letter in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(i, j, board, trie.root, visited, final_words)
    return list(final_words.keys())
    
def explore(i, j, board, trie_node, visited, final_words):
    if visited[i][j]:
        return
    letter = board[i][j]
    if letter not in trie_node:
        return
    visited[i][j] = True
    trie_node = trie_node[letter]
    if '*' in trie_node:
        final_words[trie_node['*']] = True
    neighbors = get_neighbors(i, j, board)
    for neighbor in neighbors:
        explore(neighbor[0], neighbor[1], board, trie_node, visited, final_words)
    visited[i][j] = False

def get_neighbors(i, j, board):
    neighbors = []
    if i > 0 and j > 0:
        neighbors.append([i-1, j-1])
    if i > 0 and j < len(board[0]) - 1:
        neighbors.append([i-1, j+1])
    if i < len(board) - 1 and j < len(board[0]) - 1:
        neighbors.append([i+1, j+1])
    if i < len(board) - 1 and j > 0:
        neighbors.append([i+1, j-1])
    if i > 0:
        neighbors.append([i-1, j])
    if i < len(board) - 1:
        neighbors.append([i+1, j])
    if j > 0:
        neighbors.append([i, j-1])
    if j < len(board) - 1:
        neighbors.append([i, j+1])
    return neighbors

class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = '*'
        
    def add(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr[self.end_symbol] = word
