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
                lval = self.monoid.op(
                    lval,
                    self.tree[SegmentTree.__sibling(l_i)]
                )
            l_i = lp_i

            if r_i % 2 == 0:
                rval = self.monoid.op(
                    rval,
                    self.tree[SegmentTree.__sibling(r_i)]
                )
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

    def __sibling(i):
        if i == 0:
            return None
        return ((i-1) ^ 1)+1


def solve_a58(N, queries):
    st = SegmentTree(Monoid([0]*N, max, 0))

    res = []
    for q in queries:
        # q[1]-1, q[2]-1 はリストのインデックスが 0 始まりによる調整
        if q[0] == 1:
            st.update(q[1]-1, q[2])
        else:
            res.append(st.answer_range(q[1]-1, q[2]-1))

    return res


def main():
    # assert (solve_a58(8, [
    #     [1, 3, 16],
    #     [2, 4, 7],
    #     [1, 5, 13],
    #     [2, 4, 7]])
    #     ==
    #     [0, 13])

    N, Q = map(int, input().split())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))

    res = solve_a58(N, queries)
    for r in res:
        print(r)


main()
