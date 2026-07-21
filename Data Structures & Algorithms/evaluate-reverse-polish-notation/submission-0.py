class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }
        for c in tokens:
            if c in ops:
                b, a = stack.pop(), stack.pop()
                stack.append(ops[c](a, b))
            else:
                stack.append(int(c))
        return stack[0]
        