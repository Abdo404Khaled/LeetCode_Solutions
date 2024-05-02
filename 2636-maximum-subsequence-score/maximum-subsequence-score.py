class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda x: x[1], reverse=True)

        nSum = 0
        heap = []
        res = 0

        for n1, n2 in pairs:
            nSum += n1
            heapq.heappush(heap, n1)

            if len(heap) > k:
                node = heapq.heappop(heap)
                nSum -= node
            if len(heap) == k:
                res = max(res, nSum * n2)
        
        return res
        