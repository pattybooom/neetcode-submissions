class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '{':
                stack.append('}')
            elif s[i] == '[':
                stack.append(']')

            elif stack:   
                if stack[-1] == s[i]:
                    stack.pop()
                else:
                    return False
            else:
                return False

        if stack:
            return False
        return True


            

        