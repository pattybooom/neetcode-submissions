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
        i = 0

        while i < len(s):

            if s[i] in memory:
                maxCount = max(maxCount,len(memory))
                i = lastSeen[s[i]] + 1

                if maxCount == window:
                    return window

                memory = s[i]

            else:
                memory += s[i]
                
                if len(memory) == window:
                    return window

            lastSeen[s[i]] = i
            i += 1
        
        return max(maxCount,len(memory))

    