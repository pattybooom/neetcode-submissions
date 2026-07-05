class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1 

        while rp > lp:
            mid = math.floor((lp + rp) / 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                rp = mid -1
            else:
                lp = mid + 1

        if lp == rp:
                if nums[lp] == target:
                    return lp
                return -1

        if rp < lp:
            return -1
            
            
        