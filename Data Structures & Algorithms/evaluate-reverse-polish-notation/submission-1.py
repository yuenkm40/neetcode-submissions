class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.lstrip('-').isdigit():
                stack.append(int(t))
            else:
                last = stack.pop()
                res = stack.pop()
                if t == "+":
                    res += last
                elif t == "-":
                    res -= last 
                elif t == "*":
                    res *= last 
                elif t == "/":
                    res = int(res / last)
                stack.append(res)

        return stack.pop()
                
            
        