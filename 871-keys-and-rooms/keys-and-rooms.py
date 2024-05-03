class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        q = deque([])
        q.append(rooms[0])
        visited = set()
        visited.add(0)

        while q:
            keys = q.popleft()
            for key in keys:
                if key not in visited:
                    visited.add(key)
                    q.append(rooms[key])

        return len(visited) == len(rooms)
        