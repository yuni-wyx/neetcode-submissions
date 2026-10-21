class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left = 0
        right = 0
        window_count = 0
        q = deque() 
        # deque stores index

        res = []

        while right < len(nums):
            
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            left = right - k + 1
            if q[0] < left:
                q.popleft()

            if right >= k - 1:
                res.append(nums[q[0]])

            right+=1
        return res
            
            

