class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        answer = []
        for i in range(0, len(nums)):
            if nums[i] not in answer:
                answer.append(nums[i])
        
        if len(answer) != len(nums):
            return True
        else:
            return False
    