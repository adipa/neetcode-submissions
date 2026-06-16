class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        length = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                count += 1
                print(count, nums[i])
            elif nums[i] == nums[i-1]:
                continue
            else:
                length = max(length, count)
                count = 1

        return max(length, count)


        