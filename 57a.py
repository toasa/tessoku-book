def solve_a57(next_holes, queries):
    N = len(next_holes)

    # 穴の添字が１始まりのため調整
    next_holes = [0] + next_holes

    # dp[0][i]: 穴 i から 2^0 日後の移動先の穴
    # dp[1][i]: 穴 i から 2^1 日後の移動先の穴
    # dp[2][i]: 穴 i から 2^2 日後の移動先の穴
    # dp[3][i]: 穴 i から 2^3 日後の移動先の穴
    # ...
    dp = [[0 for _ in range(N+10)] for _ in range(32)]
    for hole in range(1, N+1):
        dp[0][hole] = next_holes[hole]
    for day in range(1, 32):
        for hole in range(1, N+1):
            dp[day][hole] = dp[day-1][dp[day-1][hole]]

    res = []
    for query in queries:
        hole = query[0]
        ndays_later = query[1]

        for day in range(0, 32):
            if (1 << day) & ndays_later == (1 << day):
                hole = dp[day][hole]

        res.append(hole)

    return res


def main():
    # assert (
    #     solve_a57([1],
    #               [[1, 1],
    #                [1, 2]])
    #     == [1, 1]
    # )

    # assert (
    #     solve_a57([2, 2],
    #               [[1, 1],
    #                [1, 2],
    #                [2, 1],
    #                [2, 2]])
    #     == [2, 2, 2, 2]
    # )

    # assert (
    #     solve_a57([2, 3, 2],
    #               [[1, 1],
    #                [1, 2],
    #                [1, 3]])
    #     == [2, 3, 2]
    # )

    # assert (
    #     solve_a57([2, 4, 1, 7, 6, 5, 3],
    #               [[1, 1],
    #                [1, 5],
    #                [2, 13],
    #                [5, 999999999]])
    #     == [2, 1, 3, 6]
    # )

    N, Q = map(int, input().split())
    holes = list(map(int, input().split()))
    queries = []
    for _ in range(Q):
        q = list(map(int, input().split()))
        queries.append(q)

    res = solve_a57(holes, queries)
    for r in res:
        print(r)


main()
