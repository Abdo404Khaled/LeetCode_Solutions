class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()

        res = 0
        for student, seat in zip(students, seats):
            res += abs(student - seat)
        
        return res
            

        