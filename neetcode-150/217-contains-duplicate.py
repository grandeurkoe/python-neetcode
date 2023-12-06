class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate_check = {}
        for element in nums:
            if element not in duplicate_check:
                duplicate_check[element] = True
            else:
                return duplicate_check[element]
        return False