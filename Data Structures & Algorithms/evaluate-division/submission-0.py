class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        a - b: 4
        b - c: 1
        ab - bc: 3.25

        a - c-> 4
        b - a

        elemet to itslef 1

        build grapth for each of them undrected grpath
        a - b: n
        b - a - 1/n
        a: [[nei, value]]

        for query:
            start and end:
              do a bfs till hit target
              if hit target return cummulative score

        """
        graph = {}

        for index, equation in enumerate(equations):
            left, right = equation

            # get empty graph
            if left not in graph:
                graph[left] = []
            
            if right not in graph:
                graph[right] = []

            # build for left
            graph[left].append([right, values[index]])
            graph[right].append([left, 1 / values[index]])

        
        def expore(start_node, end):

            # get a queue

            if start_node not in graph:
                return -1
                
            queue = deque([[start_node, 1]])
            visited = set()
            

            while queue:

                # check if we have the end node
                curr_node, cost = queue.popleft()

                if curr_node == end:
                    return cost
                
                # increase the result
                visited.add(curr_node)

                for nei, c in graph[curr_node]:
                    if nei not in visited:
                        queue.append([nei, c * cost])

            return -1

        result = []
        for start, end in queries:
            res = expore(start, end)
            result.append(res)

        return result













