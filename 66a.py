import sys
sys.setrecursionlimit(10**7)


class UnionFinder:
    def __init__(self, n_node):
        self.nodes = [UnionFinder.Node(i) for i in range(n_node+1)]

    def __root(self, node):
        if node.parent == None:
            return node

        self.parent = self.__root(node.parent)
        return self.parent

    def is_connected(self, id1, id2):
        n1 = self.nodes[id1]
        n2 = self.nodes[id2]

        return self.__root(n1).id == self.__root(n2).id

    def unite(self, n1, n2):
        r1 = self.__root(self.nodes[n1])
        r2 = self.__root(self.nodes[n2])

        r1.parent = r2

    class Node:
        def __init__(self, _id):
            self.id = _id
            self.parent = None


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
