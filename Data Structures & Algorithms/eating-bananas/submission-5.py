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
        minim = 0 
        
        minK = maxim
        logH = math.log2(maxim)

        for i in range(int(logH) + 1):
            k = round((maxim + minim) / 2)
            steps = self.EatWithRateK(k, piles)
            print(f"eating with rate {k}, min: {minim}, max: {maxim}")
            if steps <= h:
                print(f"new max = {k}")
                if k < minK:
                    minK = k
                maxim = k
            else:
                print(f"new min = {k}")
                minim = k
            if minK == 1:
                return 1


        
        return minK

        
        