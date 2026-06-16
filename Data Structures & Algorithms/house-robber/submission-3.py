class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     return max(dfs(i + 1),
        #                nums[i] + dfs(i + 2))
        
        # return dfs(0)
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        
        robmoney = [0] * n

        robmoney[n - 1] = nums[n-1]
        robmoney[n - 2] = max(nums[n-2], nums[n-1])
        for i in range(n-3, -1, -1):
            a = robmoney[i+1]
            b = robmoney[i+2] + nums[i]
            print(a,b)
            robmoney[i] = max(a, b)

        print(robmoney)
        return max(robmoney[0], robmoney[1])