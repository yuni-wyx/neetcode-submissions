class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        left = 0
        right = 0
        max_length = 0

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right+=1
                max_length = max(max_length, len(seen))
            
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left+=1
        
        return max_length



