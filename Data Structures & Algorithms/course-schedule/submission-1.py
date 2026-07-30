class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # build the grapth
        # have visited
        visited = [False] * numCourses
        graph = {}

        for i in range(numCourses):
            graph[i] = []

        for course, preq, in prerequisites:
            # add the main course and prequisits
            preqsite = graph[course]
            preqsite.append(preq)
            graph[course] = preqsite

        

        # DFS
        def dfs(node, path):
            
            if node is None:
                return True

            if node in path:
                return False

            if visited[node]:
                return True 

            
            # add this to path
            path.add(node)

            # explore the neib
            for pre in graph[node]:
                
                can_take = dfs(pre, path)
                if not can_take:
                    return False
            
            path.remove(node)
            visited[node] = True
            
            return True

        
        for i in range(numCourses):
            can_take = dfs(i, set())
            if not can_take:
                return False
        
        return True


