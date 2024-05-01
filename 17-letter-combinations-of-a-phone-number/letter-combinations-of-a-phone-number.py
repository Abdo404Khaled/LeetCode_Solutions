class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
            
        keyboard = {
                '2': ['a','b','c'],
                '3': ['d','e','f'],
                '4': ['g','h','i'],
                '5': ['j','k','l'],
                '6': ['m','n','o'],
                '7': ['p','q','r', 's'],
                '8': ['t','u','v'],
                '9': ['w','x','y', 'z']
                }
        
        n = len(digits)
        res = []

        def dfs(i, temp):
            if i == n:
                res.append(temp[:])
                return
            
            for c in keyboard[digits[i]]:
                temp = temp + c
                dfs(i+1, temp)
                temp = temp[:-1]
            
        dfs(0, '')
        return res