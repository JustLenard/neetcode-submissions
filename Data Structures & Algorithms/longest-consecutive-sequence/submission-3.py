class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = sorted(set(nums))
        
        result = 0
        longest_sequence = 0
        prev = 0
        for i in range(len(nums)):
            if i == 0:
                prev = nums[i]
                longest_sequence = 1
            elif nums[i] - 1 == prev:
                prev = nums[i]
                longest_sequence += 1
            else:
                prev = nums[i]
                result = max(result, longest_sequence)
                longest_sequence = 1

        result = max(result, longest_sequence)
        return result