class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack = []

        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log == "./":
                pass
            else:
                stack.append(log.split('/')[0])
        
        print(stack)
        return len(stack)
        