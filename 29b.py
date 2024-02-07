LIMIT = 1000000007

memo = {}


def calc_power_recursive(x, n):
    # print("{} ** {}".format(x, n))
    if n in memo:
        return memo[n]

    if n // 2 in memo:
        res_half = memo[n//2]
        res = (res_half ** 2) if n % 2 == 0 else (res_half ** 2) * x
        res %= LIMIT
        memo[n] = res
        return res

    res = calc_power_recursive(x, n//2)
    memo[n] = res * res if n % 2 == 0 else res * res * x
    memo[n] %= LIMIT
    return memo[n]


def main():
    a, b = map(int, input().split())
    memo[0] = 1
    memo[1] = (a % LIMIT)

    print(calc_power_recursive(a, b))
    # print(memo)


main()
