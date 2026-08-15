class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        result = 1
        L = 0
        prev_sign = None

        for R in range(1, len(arr)):
            if arr[R] == arr[R-1]:
                curr_sign = "="
            elif arr[R] > arr[R-1]:
                curr_sign = ">"
            else:
                curr_sign = "<"
            
            if curr_sign == "=":
                L = R
                prev_sign = None
            else:
                if curr_sign == prev_sign:
                    L = R - 1
                prev_sign = curr_sign
            result = max(result, R - L + 1)
        return result
