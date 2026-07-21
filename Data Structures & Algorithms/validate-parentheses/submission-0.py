class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        oppo = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                assert c in ')]}'
                if len(stack) == 0 or stack[-1] != oppo[c]:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0
        