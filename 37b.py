from math import log10


def num_of_digit(n):
    return int(log10(n))+1


def solve_b37(N):
    n_digit = num_of_digit(N)

    digit_count = [0 for _ in range(10)]

    # 各桁ごとに、1,2,3,...の数を数え上げていく。
    for d in range(n_digit):
        keta_d = (N % (10**(d+1)))//(10**d)
        for i in range(1, 10):
            digit_count[i] += (N//(10**(d+1))) * (10**d)
        for i in range(1, keta_d):
            digit_count[i] += 10**d
        digit_count[keta_d] += N % (10**d)+1

    res = 0
    for i in range(1, 10):
        res += digit_count[i] * i

    return res


# for testing
def solve_b37_slow(N):
    res = 0
    for n in range(1, N+1):
        res += sum(list(map(int, list(str(n)))))

    return res


def test():
    assert (solve_b37(1) == 1)
    assert (solve_b37(4) == 10)
    assert (solve_b37(10) == 46)
    assert (solve_b37(11) == 48)
    assert (solve_b37(288) == 2826)
    assert (solve_b37(400) == 4204)
    assert (solve_b37(700) == 8407)


def main():
    N = int(input())
    print(solve_b37(N))


# test()
main()
