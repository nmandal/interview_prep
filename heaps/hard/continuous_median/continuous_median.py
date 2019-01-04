class ContinuousMedianHandler:
    def __init__(self):
        self.lowers = Heap(MAX_HEAP_FUNC, [])
        self.greaters = Heap(MIN_HEAP_FUNC, [])
    
    # O(log n) time | O(n) space
    def insert(self, number):
        if not self.lowers.length or number < self.lowers.peek():
            self.lowers.insert(number)
        else:
            self.greaters.insert(number)
        self.rebalance_heaps()
        self.update_median()
    
    def rebalance_heaps(self):
        if self.lowes.length - self.greaters.length == 2:
            self.greaters.insert(self.lowers.remove())
        elif self.greaters.length - self.lowers.length == 2:
            self.lowers.insert(self.greaters.remove())
    
    def update_median(self):
        if self.lowers.length == self.greaters.length:
            self.median = (self.lowers.peek() + self.greaters.peek()) / 2
        elif self.lowers.length > self.greaters.length:
            self.median = self.lowers.peek()
        else:
            self.median = self.greaters.peek()
    
    def get_median(self):
        return self.median
    
class Heap:
    def __init__(self, comparison_func, array):
        self.heap = self.build_heap(array)
        self.comparison_func = comparison_func
        self.length = len(self.heap)
    
    def build_heap(self, array):
        first_parent_idx = (len(array) - 2) // 2
        for curr_idx in reversed(range(first_parent_idx + 1)):
            self.sift_down(curr_idx, len(array) - 1, array)
        return array
    
    def sift_down(self, curr_idx, end_idx, heap):
        child_one_idx = curr_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = curr_idx * 2 + 2 if curr_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != 1:
                if self.comparison_func(heap[child_two_idx], heap[child_one_idx])):
                    idx_to_swap = child_two_idx
                else:
                    idx_to_swap = child_one_idx
            else:
                idx_to_swap = child_one_idx
            if self.comparison_func(heap[idx_to_swap], heap[curr_idx]):
                self.swap(curr_idx, idx_to_swap, heap)
                curr_idx = idx_to_swap
                child_one_idx = curr_idx * 2 + 1
            else:
                return
    
    def sift_up(self, curr_idx, heap):
        parent_idx = (curr_idx - 1) // 2
        while curr_idx > 0:
            if self.comparison_func(heap[curr_idx, heap[parent_idx]]):
                self.swap(curr_idx, parent_idx, heap)
                curr_idx = parent_idx
                parent_idx = (curr_idx - 1) // 2
            else:
                return
    
    def peek(self):
        return self.heap[0]
    
    def remove(self):
        self.swap(0, self.length - 1, self.heap)
        val_to_remove = self.heap.pop()
        self.length -= 1
        self.sift_down(0, self.length - 1, self.heap)
        return val_to_remove
    
    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self.sift_up(self.length - 1, self.heap)
    
    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]
        
def MAX_HEAP_FUNC(a, b):
    return a > b

def MIN_HEAP_FUNC(a, b):
    return a < b
