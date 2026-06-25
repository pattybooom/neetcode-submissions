class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [nums[0]]
        post = [0]*(len(nums))
        post[len(post)-1] = nums[len(nums)-1]

        for i in range(1,len(nums)):
            pre.append(nums[i]*pre[i-1])


        for i in range(len(nums)-2,-1,-1):
            print(i)
            post[i] = (nums[i] * post[i+1])


        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(post[i+1])
            elif i == len(nums) - 1:
                ans.append(pre[i-1])
            else:
                ans.append(pre[i-1] * post[i+1])
        return ans


            
            

        