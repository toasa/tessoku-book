def solve_b58(n_step, step_dists_from_start, jump_min, jump_max):
    # each_dists[i]: 足場 i から i + i までの距離
    each_dists = [0 for _ in range(n_step-1)]
    for i in range(0, n_step-1):
        each_dists[i] = step_dists_from_start[i+1]-step_dists_from_start[i]

    # dists[i][j]: 足場 i から足場 j までの距離
    dists = [[0 for _ in range(n_step+10)] for _ in range(n_step+10)]
    for i in range(n_step-1):
        for j in range(i+1, n_step):
            d = 0
            for step in range(i, j):
                d += each_dists[step]
            dists[i][j] = d

    # dp[i]: 足場 0 から足場 i まで移動する場合の、ジャンプの最小回数
    INF = 10**6
    dp = [INF for _ in range(n_step+10)]
    dp[0] = 0  # 足場 0 はスタート地点なので、必要なジャンプ回数は 0 回

    for j in range(1, n_step):
        for i in range(j):
            d = dists[i][j]
            if jump_min <= d <= jump_max:
                dp[j] = min(dp[j], dp[i]+1)

    return dp[n_step-1]


def test():
    assert (
        solve_b58(2, [0, 10], 5, 10)
        ==
        1
    )

    assert (
        solve_b58(5, [0, 20, 30, 60, 70], 20, 40)
        ==
        2
    )

    assert (
        solve_b58(4, [0, 20, 40, 60], 10, 20)
        ==
        3
    )

    assert (
        solve_b58(5, [0, 14, 15, 24, 39], 10, 15)
        ==
        3
    )


def main():
    n_step, jump_min, jump_max = map(int, input().split())
    step_dists = list(map(int, input().split()))

    print(solve_b58(n_step, step_dists, jump_min, jump_max))


# test()
main()
