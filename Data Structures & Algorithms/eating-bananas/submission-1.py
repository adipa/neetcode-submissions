class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        maxK = max(piles)
        minK = 1
        k = 0

        while(minK <= maxK):
            hours = 0
            midK = (minK + maxK) // 2
            for p in piles:
                hours += (p // midK) + (1 if p % midK else 0)
                if hours > h:
                    break
            if hours > h:
                minK = midK + 1
            else:
                maxK = midK - 1
                k = midK

        return k



        