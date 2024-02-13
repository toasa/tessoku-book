def solve_a37(N, M, A, B, C):
    res = N * M * B
    res += sum(A) * M
    res += sum(C) * N
    return res


def main():
    # assert (solve_a37(2, 3, [10, 20], 100, [1, 2, 3]) == 702)

    N, M, B = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    print(solve_a37(N, M, A, B, C))


main()
