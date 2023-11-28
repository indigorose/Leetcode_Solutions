class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        x = list(ransomNote)
        y = list(magazine)
        for char in x:
            if char in y:
                y.remove(char)
            else:
                return False
        return True