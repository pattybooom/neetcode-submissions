class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1dict = {}
        for i in range(len(s1)):
            if s1[i] not in s1dict:
                s1dict[s1[i]] = 1
            else:
                s1dict[s1[i]] += 1

        left = 0
        right = left + len(s1) - 1
        s2dict = {}
        for i in range(right+ 1):
            if s2[i] not in s2dict:
                s2dict[s2[i]] = 1
            else:
                s2dict[s2[i]] += 1


        while right < len(s2):
          
            count = 0
            for x in s1dict:
                

                if x in s2dict and s1dict[x] == s2dict[x]:
                    
                    count += s2dict[x]
                    if count == len(s1):
                        return True
                    continue
                else:
                    pass

            
            s2dict[s2[left]] -= 1
            left += 1
            right += 1
            if right < len(s2): 
                if s2[right] not in s2dict:
                    s2dict[s2[right]] = 1
                else:
                    s2dict[s2[right]] += 1

          

            
        return False