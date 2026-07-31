class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # check for cycle
        if n != len(edges) + 1:
            return False

        # build a union find by rank and path compression
        rank = [1] * n
        parent = list(range(n))

        # find algoritm
        def find(node):
            # find the parent
            if parent[node] != node:
                parent[node] = find(parent[node])
            
            return parent[node]

        
        # union two nodes
        def union(a, b):
            # find the parens
            parent_a = find(a)
            parent_b = find(b)

            # already connected
            if parent_a == parent_b:
                return False
            
            # connect them by rank
            if rank[parent_a] < rank[parent_b]:
                parent[parent_a] = parent_b
            elif rank[parent_a] > rank[parent_b]:
                parent[parent_b] = parent_a
            else:
                parent[parent_a] = parent_b
                rank[parent_b] += 1

            return True

        
        # union all vertices
        for a, b in edges:
            # union them
            union(a, b)

        root = find(0)

        for node in range(1, n):
            curr_root = find(node)
            if root != curr_root:
                return False

        
        return True

            # check if this parent is same as before






