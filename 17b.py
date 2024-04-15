def solve_b17(footings):
    # dp[i]: 足場 0 から i に移動するまでにかかる最小コスト
    dp = [0 for _ in range(len(footings)+10)]

    # prev_fotting[i]: 足場 i がいくつ前の足場から移動してきたか（-1 or -2)
    prev_footing = [-1 for _ in range(len(footings)+10)]

    # 足場 1 への移動方法は１通りなので、特別処理
    dp[1] = abs(footings[1]-footings[0])

    for i in range(2, len(footings)):
        cost_from_prev = dp[i-1]+abs(footings[i]-footings[i-1])
        cost_from_prev2 = dp[i-2]+abs(footings[i]-footings[i-2])

        if cost_from_prev <= cost_from_prev2:
            dp[i] = cost_from_prev
            prev_footing[i] = -1  # -1 で初期化してるのでほんとは不要。
        else:
            dp[i] = cost_from_prev2
            prev_footing[i] = -2

    # 辿ってきた足場を復元する
    cur = len(footings)-1
    res = []
    while cur >= 0:
        res.append(cur+1)
        cur += prev_footing[cur]

    res = res[::-1]

    return len(res), res


def test():
    assert (
        solve_b17([10, 20])
        ==
        (2, [1, 2])
    )

    assert (
        solve_b17([10, 30, 40, 20])
        ==
        (3, [1, 2, 4])
    )

    assert (
        solve_b17([10, 10])
        ==
        (2, [1, 2])
    )

    assert (
        solve_b17([30, 10, 60, 10, 60, 50])
        ==
        (4, [1, 3, 5, 6])
    )


def main():
    _ = input()
    footings = list(map(int, input().split()))

    K, P = solve_b17(footings)
    print(K)
    for i, p in enumerate(P):
        if i + 1 == len(P):
            print(p)
        else:
            print("{} ".format(p), end="")


# test()
main()
