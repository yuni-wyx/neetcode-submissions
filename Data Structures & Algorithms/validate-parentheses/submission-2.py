class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        dic = {
                ')':'(',
                '}':'{',
                ']':'['
            }

        for c in s:
            if c in dic:
                expected = dic[c]
                if not stack or expected != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0
            