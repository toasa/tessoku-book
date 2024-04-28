from math import sqrt


def dist(p1, p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def solve_b23(cities):
    INF = 10**7

    n_city = len(cities)

    # dp[S][v]: 都市 0 からスタートし、都市 {0,1,...,n-1} の部分集合 S を巡回する経路の内、移動距離の最小値。
    #           ただし、都市 v を最後に訪れたものとする。 最初に都市 0 にいることを S の lsb で表現しない。
    #           たとえば、都市の数が３の場合、以下のようになる：
    #
    #             * S = 0b010 の場合、移動 0->1 を表す。
    #             * S = 0b100 の場合、移動 0->2 を表す。
    #             * S = 0b110 の場合、移動 0->1->2, または 0->2->1 を表す。
    #             * S = 0b111 の場合、移動 0->1->2->0, または 0->2->1->0 を表す。
    #
    #           よって、DP[0b111][0] を見れば、0 へ帰る

    dp = [[INF for _ in range(n_city)] for _ in range(2**n_city)]

    # 都市 0 から、それ以外の都市への距離をメモする。
    for v in range(0, n_city):
        dp[1 << v][v] = dist(cities[0], cities[v])

    # S: 巡回済みの都市の集合
    # v: 次に訪れようとしている都市
    # u: S に含まれる都市
    for S in range(1, 2**n_city):
        for v in range(n_city):
            if (1 << v) & S == (1 << v):
                # 都市 v はすでに訪れている場合。
                continue

            min_d = INF

            # S 内の各都市 u に対し、u から v へ移動する場合の最短距離を求める。
            for u in range(n_city):
                if (1 << u) & S != (1 << u):
                    # 都市 u が巡回済みでない場合。
                    continue

                min_d = min(dp[S][u]+dist(cities[u], cities[v]), min_d)

            dp[S | (1 << v)][v] = min_d

    # for S in range(2**n_city):
    #     print(dp[S])

    return dp[2**n_city-1][0]


def test():
    def check(cities, expected):
        acceptable_error_range = 10**-3

        assert (
            abs(
                solve_b23(cities) - expected
            )
            <= acceptable_error_range
        )

    check(
        [
            [0, 0],
            [5, 0],
        ],
        10.0
    )

    check(
        [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1],
        ],
        4.0
    )

    check(
        [
            [2, 5],
            [2, 3],
            [4, 1],
            [1, 1],
            [7, 2],
            [5, 3],
            [6, 5],
        ],
        18.870481592668
    )


def main():
    N = int(input())
    cities = []
    for _ in range(N):
        x, y = map(int, input().split())
        cities.append([x, y])

    print(solve_b23(cities))


# test()
main()
