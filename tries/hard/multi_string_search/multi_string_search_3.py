# O(ns + bs) time | O(ns) space
def multi_string_search(big_string, small_strings):
    trie = Trie()
    for string in small_strings:
        trie.insert(string)
    contained_strings = {}
    for i in range(len(big_string)):
        find_small_strings_in(big_string, i, trie, contained_strings)
    return [string in contained_strings for string in small_strings]

def find_small_strings_in(string, start, trie, contained_strings):
    curr_node = trie.root
    for i in range(start, len(string)):
        curr_char = string[i]
        if curr_char not in curr_node:
            break
        curr_node = curr_node[curr_char]
        if trie.end_symbol in curr_node:
            contained_strings[curr_node[trie.end_symbol]] = True
            
class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def insert(self, string):
        curr = self.root
        for i in range(len(string)):
            if string[i] not in curr:
                curr[string[i]] = {}
            curr = curr[string[i]]
        curr[self.end_symbol] = string
