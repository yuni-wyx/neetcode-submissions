class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)

        for i in range(0, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # 當今天的溫度比stack裡的溫度高，就要結算，一次結算所有當下stack裡存的index當天的溫度
                prev = stack.pop()
                res[prev] = i - prev 
                # 因為是存位置
            stack.append(i)

        return res