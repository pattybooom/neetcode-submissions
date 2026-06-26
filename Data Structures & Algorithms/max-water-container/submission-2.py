class Solution:

    
    def maxArea(self, heights: List[int]) -> int:
        lp = 0 
        rp = len(heights) - 1
        maxA = 0

        while lp < rp:
            area = min(heights[lp],heights[rp]) * (rp - lp)

            if area > maxA:
                maxA = area    

            if heights[lp] > heights[rp]:
                rp -= 1
            elif heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1

        return maxA 
