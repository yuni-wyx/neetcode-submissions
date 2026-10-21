class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = []
        i = 0
        while i < len(nums):
            j = 0
            multi = 1
            while j < len(nums):
                if i == j:
                    j+=1
                else:
                    multi = multi * nums[j]
                    j+=1
            answer.append(multi)        
            i+=1
        return answer