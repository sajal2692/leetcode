class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        res = len(students)
        counts = Counter(students) # {1: 4, 0: 2}

        for s in sandwiches: # [1,0,0,0,1,1]
            if counts[s] > 0:
                counts[s] -= 1
                res -= 1
            else: 
                break
        return res 

# {1: 4, 0: 2} res:  6
# {1: 3, 0: 2} res: 5
# {1: 3, 0: 1} res: 4
# {1: 3, 0: 0} res: 3
