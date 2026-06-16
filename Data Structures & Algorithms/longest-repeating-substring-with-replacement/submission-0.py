class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # windowLength - maxLettCount <= k

        l, r = 0, 0
        maxWindowLength = 0
        countDict = {}

        while r < len(s):
            windowLength = r - l + 1
            countDict[s[r]] = countDict.get(s[r], 0) + 1

            if windowLength - max(countDict.values()) > k:
                countDict[s[l]] -= 1
                l += 1
            else:
                maxWindowLength = max(maxWindowLength, windowLength)

            r += 1

        return maxWindowLength


