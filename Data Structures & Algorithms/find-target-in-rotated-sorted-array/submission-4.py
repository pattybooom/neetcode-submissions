class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1

        while left != right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        right = left - 1
        if right == -1:
            right = len(nums) - 1

        leftSection = nums[:left]
        rightSection = nums[left:]

        print(leftSection)
        print(rightSection)

        if leftSection and leftSection[0] <= target <= leftSection[-1]:
            toSearch = leftSection
            buffer = 0
        else:
            toSearch = rightSection
            buffer = len(leftSection)

        left = 0
        right = len(toSearch) - 1

        while left <= right:
            mid = (left + right) // 2

            if toSearch[mid] == target:
                
                return mid + buffer
            elif toSearch[mid] > target:
                right = mid - 1

            else:

                left = mid + 1
                
        if left < len(toSearch) and toSearch[left] == target:
            return left + buffer

        return -1
