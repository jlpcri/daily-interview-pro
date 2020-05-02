
def courses_to_take(course_to_prereqs):
    # Fill this in.
    def dfs(graph, visited, visiting, course):
        visited[course] = True
        visiting[course] = True

        for reqCourse in graph[course]:
            if visiting[reqCourse]:
                return False
            elif not visited[reqCourse]:
                res = dfs(graph, visited, visiting, reqCourse)
                if not res:
                    return False

        visiting[course] = False
        result.append(course)
        return True

    visited_ = {}
    visiting_ = {}
    for item in course_to_prereqs.keys():
        visited_[item] = False
        visiting_[item] = False

    result = []
    for course_ in course_to_prereqs.keys():
        if not visited_[course_]:
            res = dfs(course_to_prereqs, visited_, visiting_, course_)
            if not res:
                return 'NULL'

            return result


courses = {
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': []
}
print(courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']