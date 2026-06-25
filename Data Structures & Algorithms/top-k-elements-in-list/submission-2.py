class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numsfreq = {}
        for num in nums:
            if num in numsfreq:
                numsfreq[num] += 1
            else:
                numsfreq[num] = 1
        out = []
        for i in range(k):
            m = max(numsfreq, key=numsfreq.get)
            out.append(m)
            numsfreq[m] = 0

        return out
            
        