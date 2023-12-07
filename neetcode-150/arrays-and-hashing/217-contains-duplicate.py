# Contains Duplicate
# Leetcode Link - https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums) -> bool:
        duplicate_check = {}
        for element in nums:
            if element not in duplicate_check:
                duplicate_check[element] = True
            else:
                return duplicate_check[element]
        return False
    
solution = Solution()
nums =  [1, 2, 3, 4]
print(f"\nnums = {nums}")
print(f"Contains Duplicate? {solution.containsDuplicate(nums)}\n")