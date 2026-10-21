class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        window_count = {}
        t_count = {}

        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        
        left = 0
        right = 0
        need = len(t_count)
        have = 0

        best_len = float("inf")
        best_start = 0

        
        while right < len(s):
            c = s[right]
            window_count[c] = window_count.get(c, 0) + 1
 
            if c in t_count and window_count[c] == t_count[c]:
                have += 1

            while have == need: #合法

                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_start = left

                left_char = s[left]
                window_count[left_char] -= 1 

                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    # 我剛剛把左邊移掉之後，這個字母的數量跌破需求了。
                    have -= 1
                left+=1
                #縮window with left
            right += 1

        if best_len == float('inf'):
            return ""

        return s[best_start: best_start+best_len]