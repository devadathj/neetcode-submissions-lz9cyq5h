class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = {i:[] for i in range(numCourses)}

        for i in prerequisites:
            course_map[i[0]].append(i[1])

        built = []
        already_built = set()

        def check_course(course_number, visited):

            visited.add(course_number)
            for i in course_map[course_number]:
                if i in visited:
                    return False

                if not check_course(i, visited):
                    return False

            if course_number not in already_built:
                built.append(course_number)
                already_built.add(course_number)
                
            course_map[course_number] = []
            visited.remove(course_number)
            return True

        for i in range(numCourses):
            if not check_course(i, set()):
                return []

        return built