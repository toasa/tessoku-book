def solve_a32(N, A, B):
    # 山札が少ない場合から多い場合に向かって、勝敗表を埋めていく。
    # こういうのも DP っていうんだよね？

    is_first_move_win = [False] * (N+10)

    # 山札がA枚未満の場合は後手必勝
    for i in range(2, A):
        is_first_move_win[i] = False

    # 山札から１パターン（A枚）だけ取り合う場合は、A枚づつ勝敗が入れ替わる。
    for i in range(A, B):
        if (i // A) % 2 == 1:
            is_first_move_win[i] = True

    for i in range(B, N+1):
        res1 = not is_first_move_win[i - A]
        res2 = not is_first_move_win[i - B]

        if res1 != res2:
            # この式違和感あるんだよな...。後手は勝敗を選べないってこと？
            #
            # いや、この式は山札が i 枚の場合の最終的な勝敗 (これ以上
            # is_first_... を更新しないため） を表しているのか。
            # i 枚の場合でも、先手から石を取っていくため、
            # 先手が勝敗を選ぶことができるなら、必ず勝ちを選ぶ。
            is_first_move_win[i] = True
        else:
            is_first_move_win[i] = res1

    return "First" if is_first_move_win[N] else "Second"


def main():
    # assert (solve_a32(8, 2, 3) == "First")
    # assert (solve_a32(6, 2, 3) == "Second")
    # assert (solve_a32(19, 2, 5) == "First")

    N, A, B = map(int, input().split())
    print(solve_a32(N, A, B))


main()
