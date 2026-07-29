class TimeMap:

    def __init__(self):
        self.tm = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        print(f"adding {value} with timestamp {timestamp} to {key}")
        kv = [value, timestamp] #e.g. [happy, 1]
        if key in self.tm: #O(n)
            self.tm[key].append(kv) 
            self.tm[key] = sorted(self.tm[key], key=lambda x: x[1]) #O(logn)

            pass
        else:
            self.tm[key] = [kv]

        print(self.tm)
        return


    

    def get(self, key: str, timestamp: int) -> str:
        #want to search for timestamp or maximum ts less than timestamp in self.tm[key]
        print(f"looking for {key} at timestamp {timestamp}")
        if key not in self.tm:
            return ""
            
        left = 0
        right = len(self.tm[key]) - 1

        if left == right: #only 1 element 
            if self.tm[key][left][1] <= timestamp:
                print(self.tm[key][left][0])
                return self.tm[key][left][0]
        while left <= right:
            
            mid = (left + right) // 2
            print(f"left is {left}")
            print(f"right is {right}")
            print(f"mid is {mid}")

            if self.tm[key][mid][1] > timestamp:
                right = mid - 1
            elif self.tm[key][mid][1] < timestamp:
                left = mid + 1
            else:
                print(self.tm[key][mid])
                return self.tm[key][mid][0]

            if self.tm[key][right][1] < timestamp:
                print(self.tm[key][right])
                return self.tm[key][right][0]
        
        return ""


            

            

            



    
