# Time Complexity - O(n) | Space Complexity - O(1)
class Solution(object):
    def isSubsequence(self, s, t):
        indx1 = 0
        indx2 = 0

        while(indx1 < len(s) and indx2 < len(t)):
            if s[indx1] == t[indx2]:
                indx1 += 1
            indx2 += 1
        
        if indx1 == len(s):
            return True
        else:
            return False