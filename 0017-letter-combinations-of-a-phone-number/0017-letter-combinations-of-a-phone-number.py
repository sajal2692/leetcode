class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        
        def helper(i, cur_str):
            if len(cur_str) == len(digits):
                res.append(cur_str)
                return
            for c in digit_to_char[digits[i]]:
                helper(i+1, cur_str+c)
        
        helper(0, "")
        return res
