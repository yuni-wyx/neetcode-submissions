class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        cars = sorted(zip(position, speed), reverse = True)
        i = 0
        current_time = 0

        
        for pos, spd in cars:
            time = (target - pos) / spd

            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
                current_time = time
            else:
                pass
        return len(stack)
