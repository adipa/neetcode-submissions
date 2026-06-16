class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        subset = []

        def generateSubsets(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            else:
                subset.append(nums[i])
                generateSubsets(i+1)
                subset.pop()
                generateSubsets(i+1)


        generateSubsets(0)
        return result

            

            
        