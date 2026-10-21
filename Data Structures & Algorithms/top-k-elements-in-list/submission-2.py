class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        answer = []
        f = {}
        for i in range(0, len(nums)):
            f[nums[i]] = f.get(nums[i], 0)+1
        
        count = 0
        while count < k:
            answer.append(max(f, key=f.get))
            del f[max(f, key=f.get)]
            count+=1
        return answer