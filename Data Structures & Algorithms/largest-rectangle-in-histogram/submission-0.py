class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        start = 0
        max_area = max(heights)

        for i in range(0, len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                area = height * (i - index)
                max_area = max(area, max_area)
                start = index

            stack.append((start, heights[i]))

        for index, height in stack:
            area = height * (len(heights)-index)
            max_area = max(area, max_area)
        return max_area

