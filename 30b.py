MOD = 1000000007


def power(a, b, mod):
    # (a**b)%mod を計算する

    # 繰り返し二乗法を使う。これは、例えば a^11 を a^8*a^2*a^1 から計算しようというアイデア。
    res = 1
    pow_a = a
    for i in range(32):
        if (1 << i) & b == (1 << i):
            res *= pow_a
            res %= mod

        pow_a = pow_a**2
        pow_a %= mod

    return res


def div(bunshi, bunbo, mod):
    # (bunshi/bunbo)%mod を計算する
    res = bunshi

    # 割り算は mod 演算で閉じていない。そのためめ、フェルマーの小定理を使い、割り算を掛け算に変形する。
    res *= power(bunbo, mod-2, mod)
    res %= mod

    return res


def combination(n, r, mod):
    # nCr を計算する

    if n-r < r:
        r = n-r

    bunbo = 1
    bunshi = 1

    for i in range(r):
        bunshi *= n-i
        bunshi %= mod

        bunbo *= r-i
        bunbo %= mod

    return div(bunshi, bunbo, mod)


def solve_b30(H, W):
    if H == 1 or W == 1:
        return 1

    # 座標 (1,1) スタートなので、マス目を数えるために 1 引く
    H -= 1
    W -= 1

    return combination(H+W, W, MOD)


def test():
    assert (power(2, 10, MOD) == 1024)
    assert (power(7, 11, MOD) == 7**11 % MOD)

    assert (combination(10, 2, MOD) == 45)
    assert (combination(13, 4, MOD) == 715)

    assert (solve_b30(1, 2) == 1)
    assert (solve_b30(5, 10) == 715)
    assert (solve_b30(869, 120) == 223713395)


def main():
    H, W = map(int, input().split())
    print(solve_b30(H, W))


# test()
main()
