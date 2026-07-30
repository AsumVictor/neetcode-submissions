"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        print(node)

        if not node:
            return None

        
        # get clone
        clone = {}

        def getClone(node):

            if node in clone:
                return clone[node]
            

            # create a clone
            neighbors = []
            new_node = Node(node.val, [])
            clone[node] = new_node

            # explore all connected and get thier neigbhors
            for nei in node.neighbors:
                nei_clone = getClone(nei)
                neighbors.append(nei_clone)
            
            new_node.neighbors = neighbors


            return new_node
        

        clone_graph = getClone(node)

        return clone_graph

        