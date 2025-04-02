# Time Complexity - O(n) | Space Complexity - O(n)
class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans = ""
        idx = 0

        for idx in range(0, len(word1)):
            ans += word1[idx]
            if idx < len(word2):
                ans += word2[idx]
        if idx < len(word2):
            ans += word2[idx+1:]

        return ans
