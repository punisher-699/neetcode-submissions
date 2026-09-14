class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        graph = [[] for _ in range(n + 1)]

        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)

        
        def dfs(source, dest, visited):
            if source == dest:
                return True
            
            visited.add(source)
            for nb in graph[source]:
                if nb not in visited:
                    if dfs(nb, dest, visited):
                        return True
            return False
        
        res = [0, 0]
        for u, v in edges:
            if not dfs(u, v, set()):
                graph[u].append(v)
                graph[v].append(u)
            else:
                res[0], res[1] = u, v
        return res