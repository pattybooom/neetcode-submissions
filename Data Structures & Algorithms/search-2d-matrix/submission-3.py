class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #search down 

        tp = 0
        bp = len(matrix) - 1
        mid = (tp + bp) // 2

        

        if matrix[mid][0] > target:
            while mid > 0 and matrix[mid][0] > target:
                mid -= 1
        else:
            while mid < len(matrix) and matrix[mid][0] <= target:
                mid += 1
            mid -= 1
        
        if matrix[mid][0] == target:
            return True

       

        #search across row we found 
        row = mid
        nums = matrix[mid]

        lp = 0
        rp = len(nums) - 1 

        while rp > lp:
            mid = math.floor((lp + rp) / 2)
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                rp = mid -1
            else:
                lp = mid + 1

        if lp == rp:
                if nums[lp] == target:
                    return True
                return False

        if rp < lp:
            return False
        return False




