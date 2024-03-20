class UnionFinder:
    def __init__(self, n_node):
        self.nodes = [UnionFinder.Node(i) for i in range(n_node+1)]

    def __root(self, node):
        cur = node
        while cur.parent != None:
            cur = cur.parent
        return cur

    def is_connected(self, id1, id2):
        n1 = self.nodes[id1]
        n2 = self.nodes[id2]

        return self.__root(n1).id == self.__root(n2).id

    def unite(self, n1, n2):
        r1 = self.__root(self.nodes[n1])
        r2 = self.__root(self.nodes[n2])

        if r1.nchild > r2.nchild:
            r1, r2 = r2, r1

        r2.nchild += r1.nchild
        r1.parent = r2

    class Node:
        def __init__(self, _id):
            self.id = _id
            self.parent = None
            self.nchild = 1


def test1():
    uf = UnionFinder(3)

    assert (uf.is_connected(1, 2) == False)
    assert (uf.is_connected(1, 3) == False)
    assert (uf.is_connected(2, 3) == False)

    uf.unite(1, 2)
    assert (uf.is_connected(1, 2) == True)
    assert (uf.is_connected(1, 3) == False)
    assert (uf.is_connected(2, 3) == False)

    uf.unite(2, 3)
    assert (uf.is_connected(1, 2) == True)
    assert (uf.is_connected(1, 3) == True)
    assert (uf.is_connected(2, 3) == True)


def test2():
    uf = UnionFinder(12)

    assert (uf.is_connected(2, 9) == False)

    uf.unite(1, 7)
    uf.unite(1, 4)

    assert (uf.is_connected(3, 6) == False)

    uf.unite(3, 5)

    assert (uf.is_connected(3, 5) == True)

    uf.unite(10, 12)
    uf.unite(4, 8)
    uf.unite(8, 11)

    assert (uf.is_connected(10, 12) == True)

    uf.unite(5, 9)

    assert (uf.is_connected(6, 8) == False)


def test3():
    uf = UnionFinder(8)

    uf.unite(2, 1)
    assert (uf.nodes[1].parent == None)
    assert (uf.nodes[2].parent.id == 1)

    uf.unite(3, 2)
    assert (uf.nodes[1].parent == None)
    assert (uf.nodes[2].parent.id == 1)
    assert (uf.nodes[3].parent.id == 1)

    uf.unite(4, 3)
    assert (uf.nodes[1].parent == None)
    assert (uf.nodes[2].parent.id == 1)
    assert (uf.nodes[3].parent.id == 1)
    assert (uf.nodes[4].parent.id == 1)

    uf.unite(5, 4)
    assert (uf.nodes[1].parent == None)
    assert (uf.nodes[2].parent.id == 1)
    assert (uf.nodes[3].parent.id == 1)
    assert (uf.nodes[4].parent.id == 1)
    assert (uf.nodes[5].parent.id == 1)

    uf.unite(7, 6)
    uf.unite(8, 6)
    assert (uf.nodes[6].parent == None)
    assert (uf.nodes[7].parent.id == 6)
    assert (uf.nodes[8].parent.id == 6)

    uf.unite(1, 6)
    assert (uf.nodes[1].nchild == 8)
    assert (uf.nodes[6].parent.id == 1)


test1()
test2()
test3()
