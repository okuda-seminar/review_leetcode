class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parents = [-1] * n
    
    def find(self, x: int) -> int:
        if self.parents[x] < 0:
            return x

        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return None
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x: int) -> int:
        return -self.parents[self.find(x)]

class UnionFindPathCompression():
    def __init__(self, n: int) -> None:
        self.parents = list(range(n))

    def find(self, x: int) -> int:
        if self.parents[x] == x:
            return x
        
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x: int, y:int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return None

        self.parents[y] = x
    
class UnionFindByRank():
    def __init__(self, n: int) -> None:
        self.parents = list(range(n))
        self.rank = [0] * n
    
    def find(self, x: int) -> int:
        if self.parents[x] == x:
            return x
        
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return None

        else:
            self.parents[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

if __name__ == '__main__':
    uf = UnionFindByRank(6)
    print(uf.parents)
    print(uf.rank)
    uf.union(0, 2)
    print(uf.parents)
    print(uf.rank)
    uf.union(1,3)
    print(uf.parents)
    print(uf.rank)
    uf.union(4,5)
    print(uf.parents)
    print(uf.rank)
    uf.union(2,4)
    print(uf.parents)
    print(uf.rank)