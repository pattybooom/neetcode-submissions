class Solution:
    def trap(self, height: List[int]) -> int:
        lp = 0
        rp = len(height) - 1
        waterSum = 0

        maxL = lp
        maxR = rp

        

        while lp < rp:
            if height[maxL] < height[maxR]:
                # left side is the limiting wall
                # calculate water at lp
                waterSum += max(0, height[maxL] - height[lp])
                # move lp right
                lp += 1
                if height[lp] > height[maxL]:
                    maxL = lp

            else:
                # right side is the limiting wall
                # calculate water at rp
                waterSum += max(0, height[maxR] - height[rp])
                # move rp left
                rp -= 1
                if height[rp] > height[maxR]:
                    maxR = rp

        

        return waterSum

    
        