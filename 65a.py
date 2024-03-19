def calc_nstaff(i, direct_staffs, memo):
    if len(direct_staffs[i]) == 0:
        memo[i] = 0
        return 1

    nstaff = 0
    for staff in direct_staffs[i]:
        nstaff += calc_nstaff(staff, direct_staffs, memo)

    memo[i] = nstaff
    return nstaff + 1


def solve_a65(N, bosses):
    direct_staffs = [[] for _ in range(N+10)]
    for i, boss in enumerate(bosses):
        direct_staffs[boss].append(i+2)

    memo = {}
    calc_nstaff(1, direct_staffs, memo)

    res = []
    for i in range(1, N+1):
        res.append(memo[i])

    return res


def test():
    assert (
        #     1 -> 2 -> 5
        #       -> 3 -> 4 -> 6
        #                 -> 7
        solve_a65(
            7,
            [1, 1, 3, 2, 4, 4],
        )
        ==
        [6, 1, 3, 2, 0, 0, 0]
    )

    assert (
        solve_a65(
            15,
            [1, 2, 1, 1, 1, 6, 2, 6, 9, 10, 6, 12, 13, 12],
        )
        ==
        [14, 2, 0, 0, 0, 8, 0, 0, 2, 1, 0, 3, 1, 0, 0]
    )

    assert (
        solve_a65(
            2,
            [1],
        )
        ==
        [1, 0]
    )

    assert (
        solve_a65(
            3,
            [1, 2],
        )
        ==
        [2, 1, 0]
    )

    assert (
        solve_a65(
            3,
            [1, 1],
        )
        ==
        [2, 0, 0]
    )

    # # 社長（社員1）をルートとする木構造から非連結な閉路を持つケース
    # assert (
    #     # 1 -> 4
    #     # 2 -> 3 -> 2
    #     solve_a65(
    #         4,
    #         [3, 2, 1],
    #     )
    #     ==
    #     [1, 1, 1, 0]
    # )

    # # 閉路に合流するパスが存在する、より複雑なケース
    # assert (
    #     # 1 -> 8
    #     # 2 -> 3 -> 4 -> 2
    #     #   -> 5 -> 6
    #     #        -> 7
    #     solve_a65(
    #         8,
    #         [4, 2, 3, 2, 5, 5, 1],
    #     )
    #     ==
    #     [1, 5, 5, 5, 2, 0, 0, 0]
    # )


def main():
    # test()

    N = int(input())
    bosses = list(map(int, input().split()))

    res = solve_a65(N, bosses)
    for i, r in enumerate(res):
        if i+1 == len(res):
            print(r)
        else:
            print("{} ".format(r), end="")


main()
