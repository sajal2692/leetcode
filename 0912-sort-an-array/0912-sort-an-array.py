class Solution:
    # insertion sort
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0 and nums[j+1] < nums[j]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                j -= 1
        return nums
    
    # merge sort
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(arr, s, e):
            
            if s >= e:
                return arr
            
            m = (s + e) // 2
            
            mergeSort(arr, s, m)
            mergeSort(arr, m + 1, e)
            
            # merge sorted halves
            merge(arr, s, m, e)
            
            return arr
        
        def merge(arr, s, m, e):
            
            # copy the two halves into individual arrays
            L = arr[s:m+1]
            R = arr[m+1:e+1]
            
            i = 0 # starting index of L
            j = 0 # starting index of L
            k = s # starting index of array
            
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
                    
            # one half will have some elements remaining
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        
        return mergeSort(nums, 0, len(nums) - 1)
    
    
#     def sortArray(self, nums: List[int]) -> List[int]:
        
#         def quickSort(arr, s, e):
            
#             # base case
#             if s >= e:
#                 return arr
            
#             pivot = arr[e]
#             left = s
#             for i in range(s, e):
#                 if arr[i] <= pivot:
#                     arr[left], arr[i] = arr[i], arr[left]
#                     left += 1
            
#             # swap pivot element with the element at left pointer
#             arr[e] = arr[left]
#             arr[left] = pivot
            
#             quickSort(arr, s, left-1)
#             quickSort(arr, left + 1, e)
            
#             return arr
        
#         return quickSort(nums, 0, len(nums) - 1)
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        