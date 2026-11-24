class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = []
        for i, num in enumerate(nums):
            prefix_to_multiply_with = 1 if i == 0 else prefix[i - 1]
            prefix.append(num * prefix_to_multiply_with)

        postfix = []
        for i, num in enumerate(nums[::-1]):
            postfix_to_multiply_with = 1 if i == 0 else postfix[i - 1]
            postfix.append(num * postfix_to_multiply_with)
        postfix = postfix[::-1]

        output = []
        for i, num in enumerate(nums):
            pre = 1 if i == 0 else prefix[i - 1]
            post = 1 if i == len(nums) - 1 else postfix[i + 1]

            output.append(pre * post)
        return output


