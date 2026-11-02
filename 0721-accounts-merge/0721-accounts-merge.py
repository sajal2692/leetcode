class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n 

    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.parent[self.parent[node]]
        node = self.parent[node]
        return self.find(node)
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        
        email_2_idx = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_2_idx:
                    uf.union(i, email_2_idx[email])
                email_2_idx[email] = i
        
        account_2_emails = defaultdict(list)
        for email, i in email_2_idx.items():
            root = uf.find(i)
            account_2_emails[root].append(email)
        
        results = []
        for a, emails in account_2_emails.items():
            result = [accounts[a][0]] + sorted(emails)
            results.append(result)
        return results

