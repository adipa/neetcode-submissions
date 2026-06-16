class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def generateSubsets(i, subset, total):
            if i == len(nums):
                return
            if total == target:
                result.append(subset.copy())
            elif total > target:
                return
            else:
                generateSubsets(i, subset + [nums[i]], total + nums[i])
                generateSubsets(i+1, subset, total)


        generateSubsets(0, subset, 0)
        return result