class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0:
            return False

        # Bucket size
        width = valueDiff + 1

        buckets = {}

        for i, num in enumerate(nums):

            # Bucket ID
            bucket = num // width

            # Check same bucket
            if bucket in buckets:
                return True

            # Check previous bucket
            if bucket - 1 in buckets:
                if abs(num - buckets[bucket - 1]) <= valueDiff:
                    return True

            # Check next bucket
            if bucket + 1 in buckets:
                if abs(num - buckets[bucket + 1]) <= valueDiff:
                    return True

            # Add current number
            buckets[bucket] = num

            # Keep only indexDiff previous elements
            if i >= indexDiff:
                old_num = nums[i - indexDiff]
                old_bucket = old_num // width
                del buckets[old_bucket]

        return False