class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the array 
        #make sure distict i 
        #left right pointer two sum 
        threes = []
        sNums = sorted(nums)

        print(sNums)
        for i in range(len(sNums) -2):
            distinct = True

            if i != 0:
                if sNums[i] == sNums[i-1]: #need to skip this 
                    distinct = False 
            
            if distinct:
                #two pointer two sum on rest of array
                lp = i+1
                rp = len(sNums) - 1
                target = -1 * sNums[i]
                

                while lp < rp:
                    pSum = sNums[lp] + sNums[rp]
                    if pSum > target:
                        rp -= 1
                        
                    elif pSum < target:
                        lp += 1
                        
                    else:
                        threes.append([sNums[i],sNums[lp],sNums[rp]])
                        olp = lp
                        while sNums[olp] == sNums[lp] and lp < len(sNums)-1:
                            olp = lp
                            lp += 1

                        orp = rp
                        while sNums[orp] == sNums[rp] and rp > i:
                            orp = rp
                            rp -= 1
                        



                

        return threes



 