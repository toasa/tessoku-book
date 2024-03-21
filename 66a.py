class UnionFinder:
    def __init__(self, n_node):
        self.nodes = [UnionFinder.Node(i) for i in range(n_node+1)]

    def __root(self, id):
        cur = self.nodes[id]
        while cur.parent != None:
            cur = cur.parent
        return cur

    def is_connected(self, id1, id2):
        return self.__root(id1).id == self.__root(id2).id

    def unite(self, id1, id2):
        r1 = self.__root(id1)
        r2 = self.__root(id2)

        if r1.id == r2.id:
            return

        if r1.nchild > r2.nchild:
            r1, r2 = r2, r1

        r2.nchild += r1.nchild
        r1.parent = r2

    class Node:
        def __init__(self, _id):
            self.id = _id
            self.parent = None
            self.nchild = 1


def solve_a66(n_node, queries):
    uf = UnionFinder(n_node)

    for q in queries:
        n1, n2 = q[1], q[2]

        if q[0] == 1:
            uf.unite(n1, n2)
        else:
            print("Yes" if uf.is_connected(n1, n2) else "No")


def main():
    N, Q = map(int, input().split())
    queries = []
    for _ in range(Q):
        q = list(map(int, input().split()))
        queries.append(q)

    solve_a66(N, queries)


main()
