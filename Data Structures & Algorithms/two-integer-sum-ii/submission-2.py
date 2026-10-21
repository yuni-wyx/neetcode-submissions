class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1

        answer = []

        while left < right:
            temp = numbers[left]+numbers[right]
            if temp == target:
                answer.append(left+1)
                answer.append(right+1)
                left += 1
            if temp < target:
                left += 1
            if temp > target:
                right -= 1
        return answer
