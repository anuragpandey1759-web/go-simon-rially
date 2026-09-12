class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # Width between the two lines
            width = right - left

            # Height is limited by the shorter line
            container_height = min(height[left], height[right])

            # Calculate area
            area = width * container_height

            # Update maximum area
            max_water = max(max_water, area)

            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
        