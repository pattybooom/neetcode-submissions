class Solution:

    

    def maxArea(self, heights: List[int]) -> int:
        def calcArea(x,y,d):
            area = min(x,y) * d
            return area

        lp = 0 
        rp = len(heights) - 1

        maxA = 0

        while lp < rp:
            d = rp - lp
            area = calcArea(heights[lp],heights[rp],d)
            print(f"{lp}, {rp}, {area}")

            if area > maxA:
                maxA = area
                print("new max")


            if heights[lp] > heights[rp]:
                rp -= 1
                
            elif heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1

        return maxA 



        
        


        # # #
        # # #