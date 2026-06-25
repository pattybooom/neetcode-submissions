class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            print(x)
            if x != "+" and x != "-" and x != "*" and x != "/":
                stack.append(x)
                print(stack)
            elif x == "+":
                a = int(stack.pop(-1))
                b = int(stack.pop(-1))
                c = a + b
                stack.append(c)
            elif x == "-":
                a = int(stack.pop(-1))
                b = int(stack.pop(-1))
                c = b - a
                stack.append(c)
            elif x == "*":
                a = int(stack.pop(-1))
                b = int(stack.pop(-1))
                c = a * b
                print(f"multiplying {a} and {b} = {c}")
                stack.append(c)
            elif x == "/":
                a = int(stack.pop(-1))
                b = int(stack.pop(-1))
                c = b / a
                stack.append(c)



        return int(stack.pop(-1))
        