class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                if sorted(subset) not in result:
                    result.append(sorted(subset.copy()))
                return
            else:
                subset.append(nums[i])
                dfs(i+1)
                subset.pop()
                dfs(i+1)

        dfs(0)
        return result
        