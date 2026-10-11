class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        # d = {}
        # for p in path:
        #     if p not in d:
        #         d[p] = 1 + d.get(p, 0)
        
        # if d['N'] != d['S'] or d['E'] != d['W']:
        #     return True
        # return False

        d = {"N" : [0, 1], "S" : [0, -1], "E" : [1, 0], "W" : [-1, 0]}

        vis = set()
        x, y = 0, 0
        for cur in path:
            vis.add((x, y))
            cx, cy = d[cur]
            x, y = x + cx, y + cy

            if (x, y) in vis:
                return True
        return False

        