class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def remove_pairs(s, a, b, value):
            stack = []
            gain = 0
            for char in s:
                if stack and stack[-1] == a and char == b:
                    stack.pop()
                    gain += value
                else:
                    stack.append(char)
            return ''.join(stack), gain
        
        if x > y:
            s, gain1 = remove_pairs(s, 'a', 'b', x)
            _, gain2 = remove_pairs(s, 'b', 'a', y)
        else:
            s, gain1 = remove_pairs(s, 'b', 'a', y)
            _, gain2 = remove_pairs(s, 'a', 'b', x)
        
        return gain1 + gain2