class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, curMult, curString = [], 0, ''
        for char in s:
            if char == '[':
                stack.append(curString)
                stack.append(curMult)
                curMult = 0
                curString = ''
            elif char == ']':
                multplier = stack.pop()
                prevString = stack.pop()
                curString = prevString + multplier * curString
            elif char.isdigit():
                curMult = curMult * 10 + int(char)
            else:
                curString += char
        return curString