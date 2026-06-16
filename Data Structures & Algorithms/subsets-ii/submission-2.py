class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            else:
                subset.append(nums[i])
                dfs(i+1)
                subset.pop()
                while i < len(nums) - 1 and nums[i+1] == nums[i]: 
                    i += 1
                dfs(i+1)
        dfs(0)
        return result
        