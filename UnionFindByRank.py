 #305. Number of Islands II
 class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parent = range(m*n)
        rank = [0 for i in range(m*n)]
        islands = [[0 for j in range(n)] for i in range(m)]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = []
        num = 0
        for position in positions:
            for direction in directions:
                newx = position[0]+direction[0]
                newy = position[1]+direction[1]
                if newx < 0 or newx > m-1 or newy < 0 or newy > n-1 or islands[newx][newy] == 0:
                    continue
                newpos = newx*n+newy
                while parent[newpos] != newpos:
                    newpos = parent[newpos]
                pos = position[0]*n+position[1]
                while parent[pos] != pos:
                    pos = parent[pos]
                if newpos != pos:
                    if rank[pos] > rank[newpos]:
                        parent[newpos] = pos
                        rank[pos] += 1
                    else:
                        parent[pos] = newpos
                        rank[newpos] += 1
                    num -= 1
            islands[position[0]][position[1]] = 1
            num += 1
            res.append(num)
        return res
