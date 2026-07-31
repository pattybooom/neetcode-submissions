class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      
        #find num of different characters 
        chars = {}
        for i in range(len(s)):
            if s[i] not in chars:
                chars[s[i]] = 1
        
        window = len(chars)

        lastSeen = {}
        memory = ""
        maxCount = 0
        left = 0
        i = left

        
        #when we see a character add its last pos to a dictionary 
        while i < len(s):
            print(s[i])
            #if we see that char again in memory then restart count from pos after last seen
            if s[i] in memory:
                maxCount = max(maxCount,len(memory))
                i = lastSeen[s[i]] + 1

                print(memory)
                if maxCount == window:
                    
                    return window
                memory = s[i]
            else:
                memory += s[i]
                if len(memory) == window:
                    
                    return window
        #if we go window without resetting then we good
            lastSeen[s[i]] = i
        #slide window decreases by 1 until found no duplicates 
            i += 1
        
        print(memory)
        return max(maxCount,len(memory))

    