# [1, 1, 0] => 6
def binarr_to_int(arr):
    res = 0
    for i, x in enumerate(reversed(arr)):
        if x == 1:
            res += 1 << i

    return res


def solve_a23(n_item, n_coupon, coupons):
    INF = 10**6

    # dp[i][j]: クーポン 1, 2,..., i から何枚か選び、商品の集合 j (j の bit 表現で商品を表す)
    #           を全て買う場合の、クーポンの最小の枚数。
    dp = [[INF for _ in range(2**n_item+10)] for _ in range(n_coupon+10)]

    # クーポン１枚目を選ぶ場合
    c1 = binarr_to_int(coupons[0])
    for j in range(1, 2**n_item):
        if j & c1 == j:
            # クーポン 1 で商品の集合 j の全ての商品を購入できる場合
            dp[0][j] = 1

    for i in range(1, n_coupon):
        c = binarr_to_int(coupons[i])
        for j in range(1, 2**n_item):
            if j & c == j:
                # クーポン i だけで、商品集合 j をカバーできる場合
                dp[i][j] = 1
            else:
                # ここむずかった。前の行の結果をそのまま見る (dp[i-1][j]) のはOK。
                # 問題は j ^ c の方。これはクーポン i-1 までがカバーする商品集合と
                # クーポン i がカバーする商品集合の和集合で、商品集合 j をカバーできる場合。
                # よくわかんなかったら、テストケース３番目の DP の配列を手書きで書いてみて。
                dp[i][j] = min(dp[i-1][j], dp[i-1][j ^ c]+1)

    # for i in range(n_coupon):
    #     print(dp[i][:8])

    if dp[n_coupon-1][2**n_item-1] != INF:
        return dp[n_coupon-1][2**n_item-1]
    else:
        return -1


def test():
    assert (
        solve_a23(1, 1, [[0]])
        ==
        -1
    )

    assert (
        solve_a23(1, 1, [[1]])
        ==
        1
    )

    assert (
        solve_a23(
            3,
            4,
            [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
                [1, 1, 0],
            ]
        )
        ==
        2
    )


def main():
    n_item, n_coupon = map(int, input().split())
    coupons = []
    for _ in range(n_coupon):
        c = list(map(int, input().split()))
        coupons.append(c)

    print(solve_a23(n_item, n_coupon, coupons))


# test()
main()
