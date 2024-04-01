def solve_a71(A, B):
    A.sort()
    B.sort(reverse=True)

    res = 0
    for a, b in zip(A, B):
        res += a*b
    return res


def test():
    assert (solve_a71([10, 20, 30], [35, 40, 33]) == 2090)


def main():
    _ = input()
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(solve_a71(A, B))


# test()
main()
