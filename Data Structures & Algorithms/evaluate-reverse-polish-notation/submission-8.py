class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        op = ['+', '-', '*', '/']
        stack = []

        for i in tokens:
            if i in op and len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    num = a + b
                elif i == '-':
                    num = a - b
                elif i =='*':
                    num = a * b
                elif i == '/':
                    num = int(a / b)
                stack.append(num)
                # 儲存是int 不是str
            if i not in op:
                stack.append(int(i))
        return int(stack[-1])