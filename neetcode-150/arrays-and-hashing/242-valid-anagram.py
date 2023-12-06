# Valid Anagram
# Leetcode Link - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            char_count = {}
            for char in s:
                if char not in char_count:
                    char_count[char] = 1
                else:
                    char_count[char] += 1
            
            for char in t:
                if char in s:
                    char_count[char] -= 1
            
            for value in char_count.values():
                if value != 0:
                    return False
            return True
        else:
            return False