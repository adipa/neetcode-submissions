from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # If the character at 'right' is already in the set, shrink the window
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # Add the current character to the set and update the max length
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
                

