class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        course_map = {i:[] for i in range(numCourses)}

        for i in prerequisites:
            course_map[i[0]].append(i[1])

        built = set()
            
        def check_course(course_number, visited):

            visited.add(course_number)
            for i in course_map[course_number]:
                if i in visited:
                    return False

                if i not in built:
                    if not check_course(i, visited):
                        return False

            built.add(course_number)
            visited.remove(course_number)
            return True

        for i in range(numCourses):
            if not check_course(i, set()):
                return False

        return True

      