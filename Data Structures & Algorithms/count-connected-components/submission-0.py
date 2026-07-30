from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # use a dfs and for a node i will visit all it neibourse and connected lyers
        # and mark them as visited.
        # now for all the nodes i will run the dfs for unvisited and count 
        # for or use bdf for it.

        # build a graph
        graph = {}
        for i in range(n):
            graph[i] = []
        
        # build the adjacenty list
        for node, nei in edges:
            graph[node].append(nei)
            graph[nei].append(node)
        

        visited_nodes = set()

        def explore(node):

            queue = deque([node])

            while queue:

                # add to visited
                cur_node = queue.popleft()
                visited_nodes.add(cur_node)

                for nei in graph[cur_node]:

                    if nei not in visited_nodes:
                        queue.append(nei)

        
        number_of_connected = 0

        for node in range(n):
            if node not in visited_nodes:
                explore(node)
                number_of_connected += 1

        
        return number_of_connected
        

