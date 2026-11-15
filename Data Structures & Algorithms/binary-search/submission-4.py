class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Base case num 1
        if len(nums) == 0:
            return -1

        middle_index = len(nums) // 2

        # Base case nr 2, aka found the target 
        if nums[middle_index] == target:
            return middle_index

        # Recursion step
        if nums[middle_index] < target:
            response  = self.search(nums[middle_index + 1:], target)
            if response == -1:
                return response
            else:
                return response + middle_index + 1
        else:
            response = self.search(nums[0: middle_index], target)
            return response


