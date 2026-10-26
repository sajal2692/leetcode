class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        N = len(edges)
        parents = {}
        rank = {}

        for i in range(1, N+1):
            parents[i] = i
            rank[i] = 0

        def find(node):
            if parents[node] == node:
                return node
            parent = find(parents[node])
            parents[node] = parent
            return parent

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] < rank[p2]:
                parents[p1] = p2
            elif rank[p2] < rank[p1]:
                parents[p2] = p1
            else:
                parents[p2] = p1
                rank[p1] += 1
            return True
        
        for edge in edges:
            n1, n2 = edge
            if not union(n1, n2):
                return edge
