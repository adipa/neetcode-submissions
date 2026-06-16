class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsDict = defaultdict(list)

        for word in strs:
            anagramsDict["".join(sorted(word))].append(word)

        print(anagramsDict.values())
        return list(anagramsDict.values())

        