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

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        #print(minCost)
        return min(cost[0], cost[1])




        