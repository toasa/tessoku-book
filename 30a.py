LIMIT = 1000000007


def calc_power(a, b, mod):
    # (a ** b) % p を計算する
    res = 1
    pow_a = a
    for i in range(30):
        if b & (1 << i) == (1 << i):
            res = (res * pow_a) % mod
        pow_a = (pow_a**2) % mod

    return res


def calc_comnination(n, r):
    # nCr を計算する
    if (n-r) < r:
        r = n-r

    if r == n:
        return 1

    res_n = 1
    res_r = 1
    for i in range(r):
        res_n *= n - i
        res_n %= LIMIT

        res_r *= r - i
        res_r %= LIMIT

    res = calc_power(res_r, LIMIT-2, LIMIT)
    res = (res * res_n) % LIMIT
    return res


def main():
    # assert (calc_comnination(3, 1) == 3)
    # assert (calc_comnination(30, 7) == 2035800)
    # assert (calc_comnination(77777, 44444) == 409085577)

    n, r = map(int, input().split())
    print(calc_comnination(n, r))


main()
