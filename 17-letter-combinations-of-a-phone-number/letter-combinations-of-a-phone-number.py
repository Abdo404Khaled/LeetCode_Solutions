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
        
        memo = {}

        def backtrack(index):
            if index == len(digits):
                return ['']

            if index in memo:
                return memo[index]

            current_digit = digits[index]
            combinations = []
            for char in keyboard[current_digit]:
                for combination in backtrack(index + 1):
                    combinations.append(char + combination)

            memo[index] = combinations
            return combinations

        return backtrack(0)