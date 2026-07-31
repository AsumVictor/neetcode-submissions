class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # 1 - 2 - 3 - 4

        # 1-2-3--4 

        # parents
        parent = {}
        rank = {}

        # find algoritm
        def find(node):
            # check if node exist
            if node not in parent:
                parent[node] = node
                rank[node] = 1

            # get the parens
            if parent[node] != node:
                parent[node] = find(parent[node])
            
            return parent[node]

        
        # union 
        def union(x, y):
            a = find(x)
            b = find(y)

            # check reducncy
            if a == b:
                return False

            # check rank
            if rank[a] < rank[b]:
                parent[a] = b
            elif rank[a] > rank[b]:
                parent[b] = a
            else:
                parent[a] = b
                rank[b] = rank[b] + 1

            return True
        

        for a, b in edges:
            
            # check if we could link
            if not union(a, b):
                return [a, b]
        
        return result

            


        