class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def rot(k):
            for i in range(0, n // 2):
                nums[i], nums[n - 1 - i] = nums[n - 1 - i], nums[i]
            print(nums)
            for i in range(0, k // 2):
                nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]
            print(nums)
            for i in range(k, (n + k) // 2):
                nums[i], nums[n + k - 1 - i] = nums[n + k - 1 - i], nums[i]
            print(nums)

        rot(k)
