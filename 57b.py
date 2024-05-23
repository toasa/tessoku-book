def sum_each_digit(N):
    res = 0

    while N != 0:
        res += N % 10
        N //= 10

    return res


def solve_b57(N, K):
    # dp[i][j]: 整数 i に対し 2**j 回操作した結果
    dp = [[0 for _ in range(35)] for _ in range(N+10)]

    # 2**0 回操作した結果を埋める
    for i in range(1, N+1):
        dp[i][0] = i-sum_each_digit(i)

    # 2**j 回操作した結果を埋める
    for i in range(1, N+1):
        for j in range(1, 33):
            # 例えば 1118 に対して 2^4 回操作した結果は、
            # 1118 に対して 2^3 回操作した結果に、さらに 2^3 回操作した結果になる。
            dp[i][j] = dp[dp[i][j-1]][j-1]

    # K の2の冪乗で表した時の、指数をメモ
    K_exp = []
    for i in range(33, -1, -1):
        if (1 << i) & K == (1 << i):
            K_exp.append(i)

    res = []
    for i in range(1, N+1):
        r = i
        for e in K_exp:
            r = dp[r][e]
        res.append(r)

    return res


def test():
    assert (sum_each_digit(1) == 1)
    assert (sum_each_digit(10) == 1)
    assert (sum_each_digit(11) == 2)
    assert (sum_each_digit(12345) == 15)

    assert (
        solve_b57(10, 1)
        ==
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 9]
    )


def main():
    N, K = map(int, input().split())

    res = solve_b57(N, K)
    for r in res:
        print(r)


# test()
main()
