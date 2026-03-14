class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_to_pre = {i: [] for i in range(numCourses)}
        for pair in prerequisites:
            course, pre = pair
            course_to_pre[course].append(pre)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if course_to_pre == []:
                return True
            
            visited.add(course)
            for pre in course_to_pre[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            course_to_pre[course] = []

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


