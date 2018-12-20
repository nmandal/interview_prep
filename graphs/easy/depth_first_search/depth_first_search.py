# O(V + E) time | O(V) space
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
    
    def add_child(self, name):
        self.children.append(Node(name))
        
    def depth_first_search(self, array):
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array
