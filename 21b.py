def solve_b21(s):
    # dp[i][j]: 文字列 s の部分文字列 s[i:j] に対して、「操作」を施して作成できる回文のうち、最長の長さ
    #
    # インデックスは inclusive に考える。例えば s="foo" の場合, dp[0][1] は "fo" を対象にする。
    dp = [[0 for _ in range(len(s)+10)] for _ in range(len(s)+10)]

    # 一文字は明らかに回文
    for i in range(len(s)):
        dp[i][i] = 1

    # DP 配列の上三角行列の部分の値を更新する。
    for wid in range(1, len(s)+1):
        for i in range(len(s)-wid):
            substr = s[i:i+wid+1]

            char_left = substr[0]
            char_right = substr[len(substr)-1]

            if char_left == char_right:
                # 左下の結果（両端の除いた場合の結果） から遷移
                dp[i][i+wid] = dp[i+1][i+wid-1] + 2
            else:
                dp[i][i+wid] = max(dp[i+1][i+wid], dp[i][i+wid-1])

    return dp[0][len(s)-1]


def test():
    assert (solve_b21("a") == 1)
    assert (solve_b21("aa") == 2)
    assert (solve_b21("ab") == 1)
    assert (solve_b21("aba") == 3)
    assert (solve_b21("abba") == 4)
    assert (solve_b21("abcb") == 3)

    # Sample test case
    assert (solve_b21("programming") == 4)
    assert (solve_b21("abcdcba") == 7)


def main():
    _ = input()
    s = input()

    print(solve_b21(s))


# test()
main()
