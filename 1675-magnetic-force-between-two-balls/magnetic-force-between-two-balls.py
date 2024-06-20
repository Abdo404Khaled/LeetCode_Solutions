class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        n=len(position)
        low=1
        high=position[-1]-position[0]
        while low<=high:
            mid=(low+high)//2
            balls_placed=1
            prev_position=position[0]
            for i in range(1,n):
                if position[i]-prev_position>=mid:
                    balls_placed+=1
                    prev_position=position[i]
            if balls_placed>=m:
                low=mid+1
                highest_force=mid
            else:
                high=mid-1
        return highest_force