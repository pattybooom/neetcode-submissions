class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        current = nums[0]
        index = 0
        last = 0

        while current != -1:
  
            last = current
            nums[index] = -1
            index = current 
            current = nums[current]
            
          
            

        return last
            


        
        