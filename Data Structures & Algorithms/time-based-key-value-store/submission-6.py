class TimeMap:

    def __init__(self):
        self.tm = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        kv = [value, timestamp] #e.g. [happy, 1]
        if key in self.tm: #O(n)
            self.tm[key].append(kv) 
   
        else:
            self.tm[key] = [kv]

        return

    def get(self, key: str, timestamp: int) -> str:
        #want to search for timestamp or maximum ts less than timestamp in self.tm[key]
        if key not in self.tm:
            return ""

        left = 0
        right = len(self.tm[key]) - 1

        if left == right: #only 1 element 
            if self.tm[key][left][1] <= timestamp:
                return self.tm[key][left][0]
        while left <= right:
            
            mid = (left + right) // 2
            if self.tm[key][mid][1] > timestamp:
                right = mid - 1
            elif self.tm[key][mid][1] < timestamp:
                left = mid + 1
            else:
                return self.tm[key][mid][0]

            if self.tm[key][right][1] < timestamp:
                return self.tm[key][right][0]
        
        return ""


            

            

            



    
