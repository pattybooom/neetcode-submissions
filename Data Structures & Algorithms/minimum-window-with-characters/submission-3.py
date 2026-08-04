class Solution:
    def minWindow(self, s: str, t: str) -> str:

        tdict = {}
        wdict = {}
        need = 0

        for letter in t:
            if letter in tdict:
                tdict[letter] += 1
                
            else:
                tdict[letter] = 1
                wdict[letter] = 0
                need += 1 

        print(need)
        left = 0 
        right = -1

        have = 0
        print(tdict)
        
        cstr = ""
        length = 10000000

        while right < len(s) + 1:
            print(wdict)
            if have == need:        
                if right - left + 1 < length:
                    cstr = s[left:right+1]
                    length = len(cstr)
                        
                #remove left most val
                if s[left] in wdict:
                    wdict[s[left]] -= 1
                    if wdict[s[left]] < tdict[s[left]]:
                        have -= 1
                left += 1
            else:
                
                right += 1
                if right < len(s):
                    print(s[right])
                    print(have)
                    current = s[right]

                    if current in tdict:
                        print(f"found a {current}")
                        wdict[current] += 1
                        print(wdict)
                        print(current)
                        if wdict[current] == tdict[current]:
                            have += 1

                        else:
                            print(f"{wdict[letter]} not equal to {tdict[letter]}")
                
            print(cstr)

        return cstr
                        
                        
                        

                


      
        