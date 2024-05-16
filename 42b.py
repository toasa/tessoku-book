from random import randint


def solve_b42(cards):
    # Score は abs(表の数字の総和) + abs(裏の数字の総和) で求まるので、二つの abs() の中身を
    # 正負どちらの方向に伸ばすか予め決める。二つの正負のパターンは以下の４通り：
    #
    #   1. 表、裏どちらも正方向
    #   2. 表が正方向、裏が負方向
    #   3. 表が負方向、裏が正方向
    #   4. 表、裏どちらも負方向
    #
    # 各パターンに対して、今見ているカードを選択すべきか O(1) で決めることができる。例えばカード [8/-3] の場合、
    # 各パターンに対するスコアは以下になる：
    #
    #   1. 8 + (-3) = 5
    #   2. 8 + -(-3) = 13
    #   3. -8 + (-3) = -13
    #   4. -8 + -(-3) = -5
    #
    # よって、パターン 1, 2 では総スコアを増やすので選択すべき。パターン 3, 4 では総スコアを減らすのでスキップすべき。

    sign_combs = [
        (True, True),  # 表、裏どちらも正
        (True, False),  # 表が正、裏が負
        (False, True),  # 表が負、裏が正
        (False, False),  # 表、裏どちらも負
    ]

    res = 0

    for s in sign_combs:
        cur_res = 0

        for c in cards:
            front, back = c[0], c[1]

            if not s[0]:
                front *= -1
            if not s[1]:
                back *= -1

            if front + back > 0:
                cur_res += front + back

        res = max(
            res,
            cur_res
        )

    return res


def solve_b42_slow(cards):
    N = len(cards)

    res = 0
    for i in range(1, 2**N):
        pick = []
        for j in range(N):
            if (1 << j) & i == (1 << j):
                pick.append(cards[j])

        total_front = 0
        total_back = 0
        for c in pick:
            total_front += c[0]
            total_back += c[1]

        res = max(res, abs(total_front)+abs(total_back))

    return res


def test():
    assert (
        solve_b42([
            [2, 8],
            [4, -5],  # pick
            [5, -3],  # pick
            [-4, 1],
            [-2, -3],  # pick
        ])
        ==
        18
    )

    assert (
        solve_b42([
            [2, 8],
            [4, -5],  # pick
            [5, -3],  # pick
            [-4, 1],
            [-2, -3],  # pick
            [-4, -1],
        ])
        ==
        18
    )

    assert (
        solve_b42([
            [4, -5],  # pick
            [5, -3],  # pick
            [-2, -3],  # pick
            [-9, -3],  # Do not pick
        ])
        ==
        18
    )

    assert (
        solve_b42([
            [100, 1],
            [100, 1],  # pick
            [100, -5],  # pick
        ])
        ==
        303
    )

    assert (
        solve_b42([
            [100, 100],
            [-180, 1],  # pick
            [-180, -1],  # pick
        ])
        ==
        360
    )

    assert (
        solve_b42([
            (1, -4),  # pick
            (3, -1),
            (-5, -10)  # pick
        ])
        ==
        18
    )

    # # Fuzzing test
    # N = 3
    # for _ in range(50):
    #     cards = [(randint(-10, 10), randint(-10, 10)) for _ in range(N)]
    #     r1 = solve_b42(cards)
    #     r2 = solve_b42_slow(cards)
    #     if r1 != r2:
    #         print(cards)
    #         print(r1, r2)


def main():
    N = int(input())
    cards = []
    for _ in range(N):
        f, b = map(int, input().split())
        cards.append((f, b))

    print(solve_b42(cards))


# test()
main()
