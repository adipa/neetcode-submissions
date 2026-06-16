class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        intSum = {}
        
        for i in range(0, len(nums)):
            if target - nums[i] in intSum.keys():
                return [intSum[target - nums[i]], i]
            intSum[nums[i]] = i
        