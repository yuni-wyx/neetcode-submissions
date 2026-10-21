class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(0, len(nums)):
            j = 0
            while j < len(nums):
                if i == j:
                    j+=1
                else:
                    if nums[i] + nums[j] == target:
                        answer.append(i)
                        answer.append(j)
                        return answer

                    else:
                        j+=1