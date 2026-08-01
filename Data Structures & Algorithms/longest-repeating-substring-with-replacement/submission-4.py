class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #start with window size 1
        window = 1
        left = 0
        right = 1 #left + window
        letters = {}
        letters[s[left]] = 1
        
        #if not we slide and doagain
        while left + window < len(s):
            #extend window to right checking if num of low freq characters < k
            right = left + window
            if s[right] not in letters:
                letters[s[right]] = 1
            else:
                letters[s[right]] += 1

            toChange = 0
            for l in letters:
                toChange += letters[l]
            toChange -= letters[max(letters, key=lambda key: letters[key])]

            #if valid inc window size 
            if toChange <= k:
                window += 1
            else:
                letters[s[left]] -= 1
                left += 1
        return window
                
            
            

