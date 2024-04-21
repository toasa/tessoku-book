def solve_b20(s1, s2):
    dp = [[0 for _ in range(len(s2)+10)] for _ in range(len(s1)+10)]

    # 初期化
    for i in range(1, len(s1)+1):
        dp[i][0] = i
    for i in range(1, len(s2)+1):
        dp[0][i] = i

    for i1, c1 in enumerate(s1):
        for i2, c2 in enumerate(s2):
            substitution_cost = 0 if c1 == c2 else 1

            dp[i1+1][i2+1] = min(
                dp[i1+1][i2] + 1,
                dp[i1][i2+1] + 1,
                dp[i1][i2] + substitution_cost,
            )

    # for i in range(len(s1)+1):
    #     print(dp[i][:len(s2)+1])

    return dp[len(s1)][len(s2)]


def test():
    assert (
        solve_b20("tokyo", "kyoto")
        ==
        4
    )

    assert (
        solve_b20("competitive", "programming")
        ==
        10
    )

    assert (
        solve_b20("abcdef", "bdf")
        ==
        3
    )


def main():
    s = input()
    t = input()

    print(solve_b20(s, t))


main()
# test()
