class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        countDict = {}

        for num in nums:
            countDict[num] = countDict.get(num, 0) + 1

        return sorted(countDict, key=countDict.get, reverse=True)[:k]
        