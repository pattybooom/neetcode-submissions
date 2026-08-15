class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numbers = {}
        for n in nums:
            if n in numbers:
                return n 
            numbers[n] = 1
        
        