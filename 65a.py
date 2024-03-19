def calc_nstaff(i, direct_staffs, memo):
    if len(direct_staffs[i]) == 0:
        memo[i] = 0
        return 1

    nstaff = 0
    for staff in direct_staffs[i]:
        nstaff += calc_nstaff(staff, direct_staffs, memo)

    memo[i] = nstaff
    return nstaff + 1


def search_loop(i, bosses):
    loop = {}

    cur = i
    while cur not in loop:
        loop[cur] = True
        cur = bosses[cur]

    return loop


def solve_a65(N, bosses):
    # インデックスを合わせる
    bosses = [-1, -1] + bosses

    direct_staffs = [[] for _ in range(N+10)]
    for i, boss in enumerate(bosses):
        direct_staffs[boss].append(i)

    memo = {}
    calc_nstaff(1, direct_staffs, memo)

    for i in range(1, N+1):
        if i not in memo:
            loop = search_loop(i, bosses)
            for j in loop:
                # `loop` には、ループを構成する頂点が重複なく入っている。
                # そのため、各頂点の部下の数は（ループの長さ）-1。
                memo[j] = len(loop) - 1

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

    # 社長（社員1）をルートとする木構造から非連結な閉路を持つケース
    assert (
        # 1 -> 4
        # 2 -> 3 -> 2
        solve_a65(
            4,
            [3, 2, 1],
        )
        ==
        [1, 1, 1, 0]
    )

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
