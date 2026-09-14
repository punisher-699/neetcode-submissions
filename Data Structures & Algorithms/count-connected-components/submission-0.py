class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for nb in graph[node]:
                if not visited[nb]:
                    dfs(nb)

        res = 0
        for node in range(n):
            if not visited[node]:
                dfs(node)
                res += 1

        return res