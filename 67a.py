class UnionTreeManager:
    def __init__(self, n_node):
        self.nodes = [UnionTreeManager.Node(i) for i in range(n_node+10)]

    def root(self, id):
        cur = self.nodes[id]
        while cur.parent != None:
            cur = cur.parent
        return cur

    def unite(self, id1, id2):
        r1 = self.root(id1)
        r2 = self.root(id2)

        if r1.id == r2.id:
            return

        if r1.nchild > r2.nchild:
            r1, r2 = r2, r1

        r1.parent = r2
        r2.nchild += r1.nchild

    def will_be_cycle(self, id1, id2):
        r1 = self.root(id1)
        r2 = self.root(id2)

        return r1.id == r2.id

    class Node:
        def __init__(self, _id):
            self.id = _id
            self.parent = None
            self.nchild = 1


def solve_a67(n_vertices, edges):
    # 辺の長さにより昇順にソート
    edges = sorted(edges, key=lambda l: l[2])

    utm = UnionTreeManager(n_vertices)

    res = 0
    for e in edges:
        if utm.will_be_cycle(e[0], e[1]):
            continue

        utm.unite(e[0], e[1])

        res += e[2]

    return res


def test():
    assert (
        solve_a67(
            7,
            [[1, 2, 12],
             [1, 3, 10],
             [2, 6, 160],
             [2, 7, 15],
             [3, 4, 1],
             [3, 5, 4],
             [4, 5, 3],
             [4, 6, 120],
             [6, 7, 14]]
        )
        ==
        55
    )


def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append([a, b, c])

    print(solve_a67(N, edges))


main()
