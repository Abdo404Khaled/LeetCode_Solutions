class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        
        sorted_meetings = sorted(meetings, key = lambda x: x[0])
        merged_meetings = [sorted_meetings[0]]
        curr_start, curr_end = sorted_meetings[0][0], sorted_meetings[0][1]
        for i in range(1, len(sorted_meetings)):
            start, end = sorted_meetings[i][0], sorted_meetings[i][1]
            if start <= curr_end:
               curr_end = max(end, curr_end)
               merged_meetings[-1][1] = curr_end
            elif curr_start < end < curr_end:
               curr_start = min(start, curr_start)
               merged_meetings[-1][0] = curr_start
            else:
                merged_meetings.append([start, end])
                curr_end = end

        ans = 0
        for i in range(len(merged_meetings)-1):
            ans += merged_meetings[i+1][0] - merged_meetings[i][1] - 1

        return ans + days - merged_meetings[-1][1] + merged_meetings[0][0] - 1

        