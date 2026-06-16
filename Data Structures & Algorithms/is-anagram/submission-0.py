class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countDict = {}
        for i in range(0, len(s)):
            countDict[s[i]] = countDict.get(s[i], 0) + 1
            countDict[t[i]] = countDict.get(t[i], 0) - 1

        for val in countDict.values():
            if val:
                return False

        return True

