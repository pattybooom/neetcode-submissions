class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #initialisation 
        indexStack = []
        heightStack = []

        indexStack.append(0)
        heightStack.append(heights[0])

        current = 1
        maxArea = 0
        while current < len(heights):
            
            

            if heightStack:
                if heights[current] >= heightStack[-1]: #just append 
                    
                    heightStack.append(heights[current])
                    indexStack.append(current)
                    
                else: #start removing stuff and calculating stuff
                    #area of last to current
                    
                    while heightStack and heights[current] < heightStack[-1]:
                        newIndex = indexStack.pop()
                        
                        area = heightStack.pop() * (current - newIndex)
                        
                        
                        maxArea = max(area,maxArea)

                    heightStack.append(heights[current])
                    indexStack.append(newIndex)
                    


            
            else:
                heightStack.append(heights[current])
                indexStack.append(current)

            current += 1


        #calc leftovers 
        while heightStack:
            height = heightStack.pop()
            width = len(heights) - indexStack.pop()

            area = height * width 
            maxArea = max(area,maxArea)



        return maxArea

                

        