from random import randint


def solve_b18(target_sum, cards):
    n_cards = len(cards)

    cards = [0] + cards

    # dp[i][j]: カード 1, 2, ..., i からいくつか選び、合計値を j にできるか？
    # B18 では選んだカードの番号を問われているので、リストを作ってメモしていく。
    dp = [[None for _ in range(target_sum+10)] for _ in range(len(cards)+10)]

    # DP 配列の1行目の更新。カード 1 を選んだ場合のメモ。
    if cards[1] <= target_sum:
        dp[1][cards[1]] = [1]

    # DP 配列の2行目以降の更新。
    for i in range(2, len(cards)):
        for t in range(target_sum+1):
            if dp[i-1][t]:
                # i-1 番目までカードをいくつか選び、合計値を t にできるケース。
                dp[i][t] = dp[i-1][t].copy()
                continue

            if t < cards[i]:
                # i 番目のカードを選ぶと、合計値 t を超えるケース。
                continue
            elif t == cards[i]:
                # i 番目のカードを選ぶと、ちょうど t になるケース。
                dp[i][t] = [i]
            else:
                if dp[i-1][t-cards[i]]:
                    dp[i][t] = dp[i-1][t-cards[i]].copy()
                    dp[i][t].append(i)

        # print("=======================================================")
        # for i in range(1, len(cards)):
        #     print(dp[i])
        # print("=======================================================")

    res = dp[n_cards][target_sum]
    if res:
        return len(res), res
    else:
        return -1


def test():
    assert (
        solve_b18(10, [10])
        ==
        (1, [1])
    )

    assert (
        solve_b18(20, [10])
        ==
        -1
    )

    assert (
        solve_b18(7, [2, 2, 3])
        ==
        (3, [1, 2, 3])
    )

    assert (
        solve_b18(7, [2, 2, 3])
        ==
        (3, [1, 2, 3])
    )

    assert (
        solve_b18(10, [1, 2, 4])
        ==
        -1
    )

    assert (
        solve_b18(9, [2, 5, 3, 8, 1])
        ==
        (3, [2, 3, 5])
    )

    assert (
        solve_b18(10000, [2, 5, 3, 8, 1])
        ==
        -1
    )

    assert (
        solve_b18(100, [14, 23, 18, 7, 11, 23, 23, 5, 8, 2])
        ==
        (6, [2, 3, 6, 7, 8, 9])
    )

    assert (
        solve_b18(4739, [6191, 4628, 2774, 5222])
        ==
        -1
    )

    # # Fuzzing test
    # for _ in range(100):
    #     N = randint(1, 60)
    #     S = randint(1, 10**4)
    #     cards = []
    #     for _ in range(N):
    #         cards.append(randint(1, 10**4))

    #     print("N={}, S={}, cards={}".format(N, S, cards))

    #     solve_b18(S, cards)


def main():
    _, target_sum = map(int, input().split())
    cards = list(map(int, input().split()))

    res = solve_b18(target_sum, cards)
    if res == -1:
        print(res)
    else:
        print(res[0])
        for i, r in enumerate(res[1]):
            if i+1 == len(res[1]):
                print(r)
            else:
                print("{} ".format(r), end="")


# test()
main()
