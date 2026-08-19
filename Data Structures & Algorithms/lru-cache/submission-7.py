class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.store = {}
        self.recent = []
        self.l = 0
        self.r = 0
        

    def get(self, key: int) -> int:
        if key in self.recent:
            self.recent.remove(key)
            self.recent.append(key)

            return self.store[key]
        return -1

    def put(self, key: int, value: int) -> None:
        
        self.store[key] = value 
        ran = self.r - self.l 

        if key in self.recent:
            self.recent.remove(key)
            self.recent.append(key)
            return



        if len(self.recent) == self.cap:
            self.recent.remove(self.recent[0])
        self.recent.append(key)

        
        
