class LRUCache:

    class ListNode:
        def __init__(self, key=None, val=None, next=None, prev=None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = self.ListNode() #least recently used 
        self.right = self.ListNode() #most recently used 

        #left point to start right point to end 
        self.left.next = self.right 
        self.right.prev = self.left 

        self.store = {} #stores {key | node}
        
    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next 
        self.store.pop(node.key)

    def insert(self,node):
        node.next = self.right
        node.prev = self.right.prev
        self.store[node.key] = node

        self.right.prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.store:
            #reinsert at end
            node = self.store[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
 
    def put(self, key: int, value: int) -> None:

        #test if node is alr in list 
        if key in self.store:
            #if so we just change the val and reinsert
            node = self.store[key]
            self.remove(node)
            self.insert(node)
            self.store[key].val = value
            return

        #if not alr in list check capacity

        node = self.ListNode(key,value)
        if self.capacity > 0:
            self.insert(node)
            self.capacity -= 1
            self.store[node.key] = node
            return
        
        #need to remove from list 
        lr = self.left.next
        self.remove(lr)
        self.insert(node)

        

    

        
        
