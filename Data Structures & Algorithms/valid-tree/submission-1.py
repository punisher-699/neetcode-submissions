class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n

        def dfs(node, parent):
            visited[node] = True

            for nb in graph[node]:
                if not visited[nb]:
                    if dfs(nb, node):
                        return True
                
                elif nb != parent:
                    return True
            return False

        count = 0
        for node in range(n):
            if not visited[node]:
                count += 1
                if dfs(node, -1):
                    return False
        return count == 1
