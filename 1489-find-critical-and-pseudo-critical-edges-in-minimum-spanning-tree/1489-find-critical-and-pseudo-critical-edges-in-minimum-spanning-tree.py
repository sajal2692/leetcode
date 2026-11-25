class UnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, node):
        while node != self.par[node]:
            self.par[node] = self.par[self.par[node]]
            node = self.par[node]
        return node
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        critical, pseudo = [], []
        for i, e in enumerate(edges):
            e.append(i) # [n1, n2, w, original_index]
        
        uf = UnionFind(n)
        mst_weight = 0
        edges.sort(key=lambda e: e[2])
        for e in edges:
            n1, n2, w, i = e
            if uf.union(n1, n2):
                mst_weight += w
        
        for n1, n2, w1, i in edges:
            weight = 0
            uf = UnionFind(n)
            for v1, v2, w2, j in edges:
                if i != j and uf.union(v1, v2):
                    weight += w2
            
            # check if edge is critical 
            if weight > mst_weight or max(uf.rank) != n:
                critical.append(i)
                continue
            
            # check if pseudo critical
            uf = UnionFind(n)
            uf.union(n1, n2)
            weight = w1
            for v1, v2, w2, j in edges:
                if uf.union(v1, v2):
                    weight += w2
            if mst_weight == weight:
                pseudo.append(i)
        
        return [critical, pseudo]

