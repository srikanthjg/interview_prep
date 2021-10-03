"""
https://leetcode.com/problems/clone-graph/
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def __init__(self):
        self.visited={}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        if node in self.visited:
            return self.visited[node]

        #list is a shallow copy
        node_copy=Node(node.val,[])

        self.visited[node]=node_copy

        for n in node.neighbors:
            ret_node=self.cloneGraph(n)
            if ret_node:
                #append each to list after creation
                node_copy.neighbors.append(ret_node)

        return node_copy
