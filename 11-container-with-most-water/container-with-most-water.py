class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_ptr, right_ptr = 0, len(height) - 1
        max_width = 0

        while left_ptr < right_ptr:
            w = right_ptr - left_ptr
            h = min(height[left_ptr], height[right_ptr])
            max_width = max(max_width, w * h)

            if height[left_ptr] <= height[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1

        return max_width