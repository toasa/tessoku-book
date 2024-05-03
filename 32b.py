def solve_b32(n_stone, takes):
    # dp[i]: のこり i 枚で自分のターンの場合の勝敗。False は負け。
    dp = [False for _ in range(n_stone+10)]

    for n_stone_remaining in range(1, n_stone+1):
        for take in takes:
            if n_stone_remaining - take >= 0 and (not dp[n_stone_remaining-take]):
                # 自分が石を take 個取ることで、相手に負け手番を渡せる場合
                dp[n_stone_remaining] = True
                break

    return "First" if dp[n_stone] else "Second"


def test():
    assert (solve_b32(8, [2, 3]) == "First")
    assert (solve_b32(6, [2, 3]) == "Second")
    assert (solve_b32(20, [6, 1, 3]) == "Second")


def main():
    n_stone, _ = map(int, input().split())
    takes = list(map(int, input().split()))

    print(solve_b32(n_stone, takes))


# test()
main()
