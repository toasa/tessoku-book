from math import log2


class Monoid:
    def __init__(self, _set, op, id_elem):
        self.set = _set
        self.op = op
        self.id_elem = id_elem


class SegmentTree:
    def __init__(self, monoid):
        self.monoid = monoid

        self.nleaf = SegmentTree.__nleaf(len(monoid.set))
        self.leaf_start_i = self.nleaf-1

        tree_len = 2**(int(log2(self.nleaf))+1)-1
        self.tree = [monoid.id_elem] * tree_len

        for i in range(len(monoid.set)):
            self.tree[self.leaf_start_i+i] = monoid.set[i]
        for i in range(self.nleaf-2, -1, -1):
            self.tree[i] = self.monoid.op(
                self.tree[SegmentTree.__left(i)],
                self.tree[SegmentTree.__right(i)],
            )

        # print(self.tree)

    def update(self, i, val):
        # モノイドのインデックスをセグメント木のインデックスへ変換
        i = i + self.leaf_start_i

        self.tree[i] = val

        # Update up to root.
        p = SegmentTree.__parent(i)
        while p != None:
            self.tree[p] = self.monoid.op(
                self.tree[SegmentTree.__left(p)],
                self.tree[SegmentTree.__right(p)],
            )
            p = SegmentTree.__parent(p)

    # 半開区間 [l, r) の要素に対し、モノイド積を適用した結果を返す
    def answer_range(self, l, r):
        l_i = l+self.leaf_start_i
        r_i = r-1+self.leaf_start_i

        if r - l == 1:
            return self.tree[l_i]

        lp_i = l_i
        rp_i = r_i
        lval = self.tree[l_i]
        rval = self.tree[r_i]
        while True:
            lp_i = SegmentTree.__parent(lp_i)
            rp_i = SegmentTree.__parent(rp_i)

            if lp_i == rp_i:
                break

            if l_i % 2 == 1:
                lval = self.tree[lp_i]
            l_i = lp_i

            if r_i % 2 == 0:
                rval = self.tree[rp_i]
            r_i = rp_i

        return self.monoid.op(lval, rval)

    def __nleaf(n):
        for i in range(1, 33):
            if n <= 2**i:
                return 2**i

    def __left(i):
        return 2*i+1

    def __right(i):
        return 2*i+2

    def __parent(i):
        return (i+1)//2-1 if i > 0 else None


class Dummy:
    def __init__(self, monoid):
        self.monoid = monoid

    def update(self, i, val):
        self.monoid.set[i] = val

    def answer_range(self, l, r):
        subset = self.monoid.set[l:r]
        res = subset[0]
        for i in range(1, len(subset)):
            res = self.monoid.op(res, subset[i])
        return res


def test1():
    A = [27, 18, 16, 37, 25, 54, 21, 11]
    st = SegmentTree(Monoid(A, max, 0))
    assert (st.tree == [54, 37, 54, 27, 37, 54,
            21, 27, 18, 16, 37, 25, 54, 21, 11])

    assert (st.answer_range(2, 3) == 16)
    assert (st.answer_range(2, 4) == 37)
    assert (st.answer_range(2, 5) == 37)
    assert (st.answer_range(2, 6) == 54)
    assert (st.answer_range(2, 8) == 54)

    st.update(2, 53)
    assert (st.tree == [54, 53, 54, 27, 53, 54,
            21, 27, 18, 53, 37, 25, 54, 21, 11])


def test2():
    A = [27, 18, 16, 37, 25, 54, 21, 11]
    st = SegmentTree(Monoid(A, max, 0))
    d = Dummy(Monoid(A, max, 0))

    for l in range(0, len(A)-1):
        for r in range(l+1, len(A)):
            assert (st.answer_range(l, r) == d.answer_range(l, r))

    st.update(2, 53)
    d.update(2, 53)
    for l in range(0, len(A)-1):
        for r in range(l+1, len(A)):
            assert (st.answer_range(l, r) == d.answer_range(l, r))


test1()
test2()
