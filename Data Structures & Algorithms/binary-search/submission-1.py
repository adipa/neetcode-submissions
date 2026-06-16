class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(l, r):

            if l > r:
                return -1

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return binarySearch(mid + 1, r)
            else:
                return binarySearch(l, mid -1)

        return binarySearch(0, len(nums) - 1)


        
        
        