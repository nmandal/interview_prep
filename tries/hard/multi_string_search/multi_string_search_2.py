# O(b^2 + ns) time | O(b^2 + n) space
def multi_string_search(big_string, small_strings):
    modified_suffix_trie = ModifiedSuffixTrie(big_string)
    return [modified_suffix_trie.contains(string) for string in small_strings]

class ModifiedSuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.populate_modified_suffix_trie_from(string)
        
    def populate_modified_suffix_trie_from(self, string):
        for i in range(len(string)):
            self.insert_substring_starting_at(i, string)
            
    def insert_substring_starting_at(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
            
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return True
        
