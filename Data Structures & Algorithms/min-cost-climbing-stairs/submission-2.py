class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memo = {}

        # def dfs(i):

        #     if i in memo:
        #         return memo[i]

        #     if i >= len(cost):
        #         return 0
            
        #     memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
        #     return memo[i]

        # return min(dfs(0), dfs(1))
        n = len(cost)
        minCost = [0] * (n)
        minCost[n - 1] = cost[n - 1]
        minCost[n - 2] = cost[n - 2]

        for i in range(n - 3, -1, -1):
            minCost[i] = cost[i] + min(minCost[i+1], minCost[i+2])
        # print(minCost)
        return min(minCost[0], minCost[1])




        