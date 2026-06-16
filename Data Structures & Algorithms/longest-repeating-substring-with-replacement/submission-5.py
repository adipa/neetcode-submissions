class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # windowLength - maxLettCount <= k

        l, r = 0, 0
        maxWindowLength = 0
        countDict = {}

        for r in range(len(s)):
            countDict[s[r]] = countDict.get(s[r], 0) + 1

            while (r - l + 1) - max(countDict.values()) > k:
                countDict[s[l]] -= 1
                l += 1

            maxWindowLength = max(maxWindowLength, (r - l + 1))

        return maxWindowLength


