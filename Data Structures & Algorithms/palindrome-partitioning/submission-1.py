class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result = []
        pals = []
        palsSet = set()

        def checkPalindrome(i,j):
            while(i < j):
                if (i, j) in palsSet:
                    return True
                elif s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            palsSet.add((i,j))
            return True

        def dfs(i):
            if i == len(s):
                result.append(pals.copy())
                return

            for j in range(i, len(s)):
                if checkPalindrome(i, j):
                    pals.append(s[i:j+1])
                    dfs(j+1)
                    pals.pop()
        dfs(0)
        return result
        