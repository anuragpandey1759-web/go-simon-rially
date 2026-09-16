class Solution:
    def numberOfArithmeticSlices(self, nums):
        if len(nums) < 3:
            return 0

        count = 0
        current = 0

        for i in range(2, len(nums)):
            # Check whether the last 3 elements form an arithmetic sequence
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                current += 1
                count += current
            else:
                current = 0

        return count