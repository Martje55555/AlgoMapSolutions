# Time Complexity - O(n) | Space Complexity - O(n)
class Solution(object):
    def romanToInt(self, s):
        mapper = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,'M': 1000}

        if s in mapper.keys():
            return mapper[s]
        
        chars = list(s)
        answer = 0
        i = 0
        while i < len(chars):
            if chars[i] == 'I' and i+1 < len(chars):
                if chars[i+1] == 'V' or chars[i+1] == 'X':
                    answer += (mapper[chars[i+1]] - mapper[chars[i]])
                    i += 1
                else:
                    answer += mapper[chars[i]]
            elif chars[i] == 'X' and i+1 < len(chars):
                if chars[i+1] == 'L' or chars[i+1] == 'C':
                    answer += (mapper[chars[i+1]] - mapper[chars[i]])
                    i += 1
                else:
                    answer += mapper[chars[i]]
            elif chars[i] == 'C' and i+1 < len(chars):
                if chars[i+1] == 'D' or chars[i+1] == 'M':
                    answer += (mapper[chars[i+1]] - mapper[chars[i]])
                    i += 1
                else:
                    answer += mapper[chars[i]]
            else:
                answer += mapper[chars[i]]
            i += 1
        return answer