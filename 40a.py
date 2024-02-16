def combination(n, r):
    res = 1
    res_r = 1
    for i in range(r):
        res *= (n - i)
        res_r *= (i + 1)
    return res // res_r


def solve_a40(N, A):
    bou_count = [0] * 110
    for a in A:
        bou_count[a] += 1

    res = 0
    for n in bou_count:
        if n < 3:
            continue

        res += combination(n, 3)

    return res


def main():
    assert (solve_a40(7, [1, 2, 1, 2, 1, 2, 1]) == 5)

    N = int(input())
    A = list(map(int, input().split()))

    print(solve_a40(N, A))


main()
