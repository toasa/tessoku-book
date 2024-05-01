import sys

sys.setrecursionlimit(10**5)


class SegTree:
    def __init__(self, arr, op, id_elem):
        # 最下段のノードの数を N とする。
        N = 1
        while N < len(arr):
            N *= 2

        # セグメント木のノード全体は N + (N-1) 個ある。
        nodes = [id_elem for _ in range(2*N-1)]

        # ノードの初期化
        #   最下段のノードは元の配列の要素をそのまま入れる。
        for i in range(min(N, len(arr))):
            nodes[i+N-1] = arr[i]
        #   それ以外のノードは、子ノードから計算する。
        for i in range(N-2, -1, -1):
            nodes[i] = op(nodes[2*i+1], nodes[2*i+2])

        self.n_leaf = N  # leaf の数は２の冪乗
        self.nodes = nodes
        self.op = op
        self.id_elem = id_elem

    # i 番目の要素の値を val に更新する
    def update(self, i, val):
        node_i = self.n_leaf-1+i

        # 末端のノードを更新
        self.nodes[node_i] = val

        parent_i = (node_i-1)//2

        # 親ノードの更新。ルートまで遡る。
        while parent_i >= 0:
            self.nodes[parent_i] = self.op(
                self.nodes[parent_i*2+1],
                self.nodes[parent_i*2+2],
            )
            parent_i = (parent_i-1)//2

    # 区間 [l, r) に対して、 self.op を施した結果を返す
    def query(self, l, r):
        return SegTree.__query(self, l, r, 0, 0, self.n_leaf)

    # ノード k に対する右半開区間 [k_l, k_r) を考える
    def __query(self, l, r, k, k_l, k_r):
        # 区間 [l, r) が区間 [k_l, k_r) を完全に被覆する場合
        if l <= k_l and k_r <= r:
            return self.nodes[k]

        # 全く被覆しない場合
        if k_r <= l or r <= k_l:
            # 単位
            return self.id_elem

        # 部分的に被覆する場合
        v_l = SegTree.__query(self, l, r, 2*k+1, k_l, (k_l+k_r)//2)
        v_r = SegTree.__query(self, l, r, 2*k+2, (k_l+k_r)//2, k_r)
        return self.op(v_l, v_r)


def main():
    # https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_A

    N, Q = map(int, input().split())

    queries = []
    for _ in range(Q):
        q = list(map(int, input().split()))
        queries.append(q)

    INF = 2**31-1
    arr = [INF for _ in range(N)]
    st = SegTree(arr, min, INF)

    for q in queries:
        if q[0] == 0:
            # update
            st.update(q[1], q[2])
        else:
            # find
            print(st.query(q[1], q[2]+1))


main()
