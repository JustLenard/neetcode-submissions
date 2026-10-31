class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx in range(len(nums)):
            num = nums[idx]
            desired_pair_for_num = target - num

            if str(desired_pair_for_num) in hash_map:
                return [hash_map[str(desired_pair_for_num)], idx]
            else:
                hash_map[str(num)] = idx