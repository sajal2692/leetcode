class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary to track numbers and their index
        num_2_index = {}
        # iterate over the numbers in the list
        for i in range(len(nums)):
            num = nums[i]
            # calculate diff in the current number and target
            difference = target - num
            # if the difference, i.e. the number we are looking for exists in the num_2_index
            if difference in num_2_index:
                # return the current infex and the index of the other number
                return [i, num_2_index[difference]]
            # add the number and its index to the dictionary
            num_2_index[num] = i