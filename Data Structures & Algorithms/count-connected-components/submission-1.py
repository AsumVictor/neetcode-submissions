class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        """
        n - components
        a, b = components - 1
        5 - 3 = 2

        5 - 4

        """

        rank = [1] * n
        parent = list(range(n))

        # find algorihtm
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            
            return parent[node]

        
        # union
        def union(a, b):
            p_a = find(a)
            p_b = find(b)


            if p_a == p_b:
                return False

            
            # join them
            if rank[p_a] < rank[p_b]:
                parent[p_a] = p_b
            elif rank[p_a] > rank[p_b]:
                parent[p_b] = p_a
            else:
                parent[p_a] = p_b
                rank[p_b] += 1

            return True

        
        components = n
        for a, b in edges:
            if union(a, b):
                components -= 1

        return components


