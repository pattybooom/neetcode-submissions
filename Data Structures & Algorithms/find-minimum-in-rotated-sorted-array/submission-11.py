class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = 1000
        left = 0 
        right = len(nums) - 1

        while left != right:
            mid = (left + right) // 2

            if nums[mid] < nums[left]:
                print(f"{nums[mid]} < {nums[left]} so switch between {nums[left]} and {nums[mid]}")
                right = mid

            elif nums[mid] > nums[right]:
                print(f"{nums[mid]} > {nums[right]} so switch between {nums[mid + 1]} and {nums[right]}")
                left = mid + 1

            else:
                right = mid


        return nums[left]





            



        
        