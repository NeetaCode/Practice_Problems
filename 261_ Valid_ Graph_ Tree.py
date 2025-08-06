from typing import List

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True  # use capital T in True

        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False  # use capital F in False

            visit.add(i)

            for j in adj[i]:
                if j == prev:
                    continue

                if not dfs(j, i):  # fixed missing colon
                    return False

            return True

        return dfs(0, -1) and len(visit) == n
