class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}  # Map key to Node
        
        # 1. Setup the Two Dummy Nodes
        self.left = Node()  # LRU bumper
        self.right = Node() # MRU bumper
        
        # Link them together initially
        self.left.next = self.right
        self.right.prev = self.left

    # --- HELPER FUNCTIONS ---
    def remove(self, node):
        # Unlink a node from wherever it is. 
        # (No edge cases because the dummy bumpers always exist!)
        prev_node = node.prev
        nxt_node = node.next
        
        prev_node.next = nxt_node
        nxt_node.prev = prev_node

    def insert(self, node):
        # Always insert directly BEFORE the Right Dummy (MRU position)
        prev_node = self.right.prev
        nxt_node = self.right
        
        prev_node.next = node
        node.prev = prev_node
        
        node.next = nxt_node
        nxt_node.prev = node
    # ------------------------

    def get(self, key: int) -> int:
        if key in self.mapping:
            # Move to most recently used: Remove it, then re-insert it!
            self.remove(self.mapping[key])
            self.insert(self.mapping[key])
            return self.mapping[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.remove(self.mapping[key])
            
        self.mapping[key] = Node(key, value)
        self.insert(self.mapping[key])
        
        # Evict the LRU if capacity is exceeded
        if len(self.mapping) > self.capacity:
            # The LRU is ALWAYS the node directly after the Left Dummy
            lru = self.left.next
            self.remove(lru)
            del self.mapping[lru.key]