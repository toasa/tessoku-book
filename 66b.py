class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)  # union 時に使用。ランクの高い方を親にする。

    # 要素 x のルートを見つける
    def find(self, x):
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])  # 経路圧縮
        return self.parent[x]

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

    def is_same(self, x, y):
        return self.find(x) == self.find(y)


def solve_b66(N, _edges, queries):
    edges = []
    for e in _edges:
        edges.append([e, True])  # クエリで削除されるパスには False をマークする

    for q in queries:
        if q[0] == 1:
            edges[q[1]-1][1] = False

    uf = UnionFind(N)
    for e in edges:
        if e[1]:
            uf.union(e[0][0], e[0][1])

    res = []
    for q in reversed(queries):
        if q[0] == 1:
            x, y = edges[q[1]-1][0]
            uf.union(x, y)
        else:
            x, y = q[1], q[2]
            res.append("Yes" if uf.is_same(x, y) else "No")

    res.reverse()

    return res


def test():
    assert (
        solve_b66(
            2,
            [(1, 2)],
            [
                (2, 1, 2),
                (1, 1),
                (2, 1, 2),
            ]
        )
        ==
        ["Yes", "No"]
    )


def main():
    N, M = map(int, input().split())
    _edges = []
    for _ in range(M):
        x, y = map(int, input().split())
        _edges.append((x, y))

    Q = int(input())
    queries = []
    for _ in range(Q):
        q = tuple(map(int, input().split()))
        queries.append(q)

    res = solve_b66(N, _edges, queries)
    for r in res:
        print(r)


# test()
main()
