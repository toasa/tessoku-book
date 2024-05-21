def c_to_n(c):
    return ord(c)-ord('a')+1


mod = 998244353


def hash(H, B_power, l, r):
    h = H[r]-(B_power[r-l+1]*H[l-1] % mod)
    if h < 0:
        h += mod
    return h


def solve_b56(S, queries):
    N = len(S)
    B = 100  # 教科書に従い 100 進数を使う
    H = [0 for _ in range(N+10)]  # 文字列 S[0:i+1]のハッシュ値
    H_rev = [0 for _ in range(N+10)]  # 文字列 S の逆順のハッシュ値
    S_rev = S[::-1]

    for i in range(1, N+1):
        H[i] = (B * H[i-1] + c_to_n(S[i-1])) % mod
    for i in range(1, N+1):
        H_rev[i] = (B * H_rev[i-1] + c_to_n(S_rev[i-1])) % mod

    B_power = [1 for _ in range(N+10)]
    for i in range(1, N+1):
        B_power[i] = (B_power[i-1]*B) % mod

    res = []
    for q in queries:
        l = q[0]
        r = q[1]

        r_rev = N-l+1
        l_rev = N-r+1

        h1 = hash(H, B_power, l, r)
        h2 = hash(H_rev, B_power, l_rev, r_rev)

        if h1 == h2:
            res.append(True)
        else:
            res.append(False)

    return res


def test():
    assert (
        solve_b56(
            "mississippi",
            [
                (5, 8),
                (6, 10),
                (2, 8),
            ]
        )
        ==
        [
            True,
            False,
            True,
        ]
    )


def main():
    _, n_query = map(int, input().split())
    S = input()
    queries = []
    for _ in range(n_query):
        x, y = map(int, input().split())
        queries.append((x, y))

    res = solve_b56(S, queries)
    for r in res:
        print("Yes" if r else "No")


# test()
main()
