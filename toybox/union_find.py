class UnionFind:
    def __init__(self, n_node):
        self.parent = list(range(n_node+1))
        self.rank = [0] * (n_node+1)

    def find(self, x):
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])  # 経路圧縮
        return self.parent[x]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_y] < self.rank[root_x]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


def test1():
    uf = UnionFind(3)

    assert (uf.is_same(1, 2) == False)
    assert (uf.is_same(1, 3) == False)
    assert (uf.is_same(2, 3) == False)

    uf.union(1, 2)
    assert (uf.is_same(1, 2) == True)
    assert (uf.is_same(1, 3) == False)
    assert (uf.is_same(2, 3) == False)

    uf.union(2, 3)
    assert (uf.is_same(1, 2) == True)
    assert (uf.is_same(1, 3) == True)
    assert (uf.is_same(2, 3) == True)


def test2():
    uf = UnionFind(12)

    assert (uf.is_same(2, 9) == False)

    uf.union(1, 7)
    uf.union(1, 4)

    assert (uf.is_same(3, 6) == False)

    uf.union(3, 5)

    assert (uf.is_same(3, 5) == True)

    uf.union(10, 12)
    uf.union(4, 8)
    uf.union(8, 11)

    assert (uf.is_same(10, 12) == True)

    uf.union(5, 9)

    assert (uf.is_same(6, 8) == False)


test1()
test2()
