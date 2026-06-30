class Solution:
    def trap(self, height: List[int]) -> int:
        lp = 0
        rp = len(height) - 1
        waterSum = 0

        maxL = height[lp]
        maxR = height[rp]

        while lp < rp:
            if maxL < maxR:
                
                # left side is the limiting wall
                # calculate water at lp
                waterSum += max(0, maxL - height[lp])
                # move lp right
                lp += 1
                
                if height[lp] > maxL:
                    maxL = height[lp]

            else:
                # right side is the limiting wall
                # calculate water at rp
                waterSum += max(0, maxR - height[rp])
                # move rp left
                rp -= 1
                if height[rp] > maxR:
                    maxR = height[rp]

        return waterSum

    
        