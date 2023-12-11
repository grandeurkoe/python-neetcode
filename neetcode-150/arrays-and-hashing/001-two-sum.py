# Two Sum
# Leetcode Link - https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        for first_idx in range(len(nums)):
            for second_idx in range(first_idx + 1, len(nums)):
                if nums[first_idx] + nums[second_idx] == target:
                    return [first_idx, second_idx]


solution = Solution()
nums = [3, 2, 4]
target = 6
print(f"\nnums = {nums}\ntarget = {target}")
print(f"\nTwo Sum : Index{solution.twoSum(nums, target)}\n")