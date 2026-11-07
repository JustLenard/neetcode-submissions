class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(nums)

        temp_longest_sequece, longest_sequece, last_number =1, 1, nums[0]

        for i in range(1, len(nums)):
            if last_number == nums[i]:
                continue
            if last_number + 1 == nums[i]:
                temp_longest_sequece +=1
                longest_sequece = max(temp_longest_sequece, longest_sequece)
            else:
                temp_longest_sequece = 1
            last_number = nums[i]
        return longest_sequece
