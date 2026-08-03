class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0 
        right = left + k
        arr = []

        while right < len(nums) + 1:
            window = [nums[i] for i in range(left,right)]

            arr.append(max(window))
            left += 1
            right += 1

        return arr