class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        s = s.replace(" ", "")
        sp = 0
        ep = len(s) - 1

        

        while sp < ep:
            print(f"{sp}, {ep}")
            while s[sp].isalnum() == False:
                sp += 1
                if sp == len(s):
                    return True
            while s[ep].isalnum() == False:
                ep -= 1
                if ep == -1:
                    return True
            if s[sp] != s[ep]:
                return False
            sp += 1
            ep -= 1
        return True 
            

             