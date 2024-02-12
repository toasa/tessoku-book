def solve_a36(N, K):
    if K < (N-1)*2:
        return "No"

    nokori_step = K - (N-1)*2

    return "Yes" if nokori_step % 2 == 0 else "No"


def main():
    # assert (solve_a36(5, 10) == "Yes")

    N, K = map(int, input().split())
    print(solve_a36(N, K))


main()
