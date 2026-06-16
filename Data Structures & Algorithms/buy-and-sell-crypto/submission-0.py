class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        r = 1
        maxProf = 0
        while r < len(prices):
            if prices[r] >= prices[l]:
                maxProf = max(maxProf, prices[r] - prices[l])
                print(maxProf)
                r += 1
            else:
                l += 1

        return maxProf
        