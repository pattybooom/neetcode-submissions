class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashNum = set()
        for i in range(len(nums)):
            hashNum.add(nums[i])

        def check(curr: int):
            runs = 0
            if curr in hashNum:
                runs += 1
                hashNum.remove(curr)

                runs += check(curr -1)
                runs += check(curr +1)
            return runs

        max = 0
        while hashNum:
            next = hashNum.pop()
            hashNum.add(next)
            
            run = check(next)
            if run > max:
                max = run
            run = 0

        return max

        


        
        

            

        