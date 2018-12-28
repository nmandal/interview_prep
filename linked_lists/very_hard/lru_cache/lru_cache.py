class LRUCache:
    def __init__(self, max_size):
        self.cache = {}
        self.max_size = max_size or 1
        self.current_size = 1
        self.list_of_most_recent = DoublyLinkedList()
        
    # O(1) time | O(1) space
    def insert_key_value_pair(self, key, value):
        if key not in self.cache:
            if self.current_size == self.max_size:
                self.evict_least_recent()
            else:
                self.current_size +=1
            self.cache[key] = DoublyLinkedListNode(key, value)
        else:
            self.replace_key(key, value)
        self.update_most_recent(self.cache[key])
    
    # O(1) time | O(1) space
    def get_value_from_key(self, key):
        if key not in self.cache:
            return None
        self.update_most_recent(self.cache[key])
        return self.cache[key].value
    
    # O(1) time | O(1) space
    def get_most_recent_key(self):
        return self.list_of_most_recent.head.key
    
    def evict_least_recent(self):
        key_to_remove = self.list_of_most_recent.tail.key
        self.list_of_most_recent.remove_tail()
        del self.cache[key_to_remove]
        
    def update_most_recent(self, node):
        self.list_of_most_recent.set_head_to(node)
        
    def replace_key(self, key, value):
        if key not in self.cache:
            raise Exception("The provided key isn't in the cache!")
        self.cache[key].value = value
        
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def set_head_to(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.remove_tail()
            node.remove_bindings()
            self.head.prev = node
            node.next = self.head
            self.head = node
    
    def remove_tail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None
    
class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
    def remove_bindings(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None
