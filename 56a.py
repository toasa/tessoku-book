def c_to_n(c):
    return ord(c) - ord('a') + 1
    # return ord(c) - ord('a')


def solve_a56(S, N, queries):
    mod = 998244353

    # 教科書通り100進数で計算
    base = 100

    # hash_memo[i] := S[0:i+1] のハッシュ値を格納する配列
    hash_memo = [0] * (N+10)
    for i in range(1, N+1):
        hash_memo[i] = (hash_memo[i-1] * base + c_to_n(S[i-1])) % mod

    power_base_memo = [1] * (N+10)
    for i in range(1, N+1):
        power_base_memo[i] = (power_base_memo[i-1] * base) % mod

    res = []

    for q in queries:
        s1_hash = hash_memo[q[1]] - \
            (power_base_memo[q[1]-q[0]+1] * hash_memo[q[0]-1]) % mod
        if s1_hash < 0:
            s1_hash += mod

        s2_hash = hash_memo[q[3]] - \
            (power_base_memo[q[3]-q[2]+1] * hash_memo[q[2]-1]) % mod
        if s2_hash < 0:
            s2_hash += mod

        res.append(True if s1_hash == s2_hash else False)

    return res


def main():
    # assert (solve_a56("abcbabc",
    #                   7,
    #                   [[1, 3, 5, 7],
    #                    [1, 5, 2, 6],
    #                    [1, 2, 6, 7]])
    #         == [True, False, False])

    # assert (solve_a56("abcfoofoo",
    #                   9,
    #                   [[1, 3, 4, 6],
    #                    [4, 6, 7, 9]])
    #         == [False, True])

    # assert (solve_a56("foofoofoo",
    #                   9,
    #                   [[1, 6, 4, 9]])
    #         == [True])

    N, Q = map(int, input().split())
    S = input()
    queries = []
    for _ in range(Q):
        q = list(map(int, input().split()))
        queries.append(q)

    res = solve_a56(S, N, queries)
    for r in res:
        print("Yes" if r else "No")


main()
