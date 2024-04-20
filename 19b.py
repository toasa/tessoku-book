def solve_b19(capacity_limit, items):
    INF = 1 << 60

    MAX_VALUE = 10**5

    # dp[i][j]: 商品 0 から i までのいくつかを選ぶとき、総価値が j 以上となるような選び方のうち、最小の総重量
    dp = [[INF for _ in range(MAX_VALUE+10)]for _ in range(len(items)+10)]

    # 最初の行の初期化
    for val in range(MAX_VALUE, -1, -1):
        w = items[0][0]
        v = items[0][1]

        if val <= v:
            dp[0][val] = w

    for i in range(1, len(items)):
        w = items[i][0]
        v = items[i][1]
        for val in range(MAX_VALUE, -1, -1):
            # val < v だとダメ。理由は、その不等式だと、else 節で val==v の場合を処理する必要があり、
            # DP 配列のインデックスの意味より、総価値が 0 以上となる場合の商品の選び方を考慮する必要がある。
            # しかし、問題の条件より各商品は 1 以上の価値を持つので、この場合は不適。
            if val <= v:
                dp[i][val] = min(dp[i-1][val], w)
            else:
                dp[i][val] = min(dp[i-1][val], w + dp[i-1][val-v])

    for val in range(MAX_VALUE, 0, -1):
        if dp[len(items)-1][val] <= capacity_limit:
            return val

    assert (False)


def test():
    assert (
        solve_b19(
            8,
            [
                [3, 30],
                [4, 50],
                [5, 60],
            ]
        )
        ==
        90
    )

    assert (
        solve_b19(
            1000000000,
            [
                [1000000000, 10],
            ]
        )
        ==
        10
    )

    assert (
        solve_b19(
            7,
            [
                [3, 13],
                [3, 17],
                [5, 29],
                [1, 10],
            ]
        )
        ==
        40
    )

    assert (
        solve_b19(
            15,
            [
                [6, 5],
                [5, 6],
                [6, 4],
                [6, 6],
                [3, 5],
                [7, 2],
            ]
        )
        ==
        17
    )

    assert (
        solve_b19(
            100,
            [
                [55, 2],
                [75, 3],
                [40, 2],
            ]
        )
        ==
        4
    )

    assert (
        solve_b19(
            1000000000,
            [
                [80000000, 99],
                [11000000, 119],
                [12000000, 150],
                [15000000, 174],
                [16000000, 168],
                [18000000, 190],
                [19000000, 187],
                [25000000, 273],
                [28000000, 307],
                [30000000, 319],
            ]
        )
        ==
        1986
    )


def main():
    N, W = map(int, input().split())
    items = []
    for _ in range(N):
        item = list(map(int, input().split()))
        items.append(item)

    print(solve_b19(W, items))


# test()
main()
