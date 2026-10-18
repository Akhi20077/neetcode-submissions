class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettersInS = {}
        lettersInC = {}

        for c in s:
            lettersInS[c] = lettersInS.get(c, 0) + 1
        
        for c in t:
            lettersInC[c] = lettersInC.get(c, 0) + 1
        
        return lettersInS == lettersInC
