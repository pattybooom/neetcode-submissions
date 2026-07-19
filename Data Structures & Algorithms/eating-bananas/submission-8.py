class Solution:
    def EatWithRateK(self, k: int, piles: List[int] ) -> int:
        h = 0
        for p in piles:
            if p % k != 0:
                h += 1
            h += p // k
        return h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxim = max(piles)
        minim = 1
        minK = maxim
        logH = math.log2(maxim)
        count = 0

        while minim < maxim:
     
            k = ((maxim + minim) // 2)
            steps = self.EatWithRateK(k, piles)

            if steps <= h:
                if k < minK:
                    minK = k
                maxim = k

            else:
                minim = k + 1
            if minK == 1:
                return 1

        return minK

        
        