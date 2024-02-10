def calc_a31(N):
    # 1 以上 N 以下の整数のうち、3 か 5 のいずれかで割り切れるものの個数を求める。

    count_total = N
    count_divisible_3 = N // 3
    count_divisible_5 = N // 5
    count_divisible_15 = N // 15

    # print("total:", count_total)
    # print("# div3:", count_divisible_3)
    # print("# div5:", count_divisible_5)
    # print("# div15:", count_divisible_15)

    count_complement = count_total + count_divisible_15 - \
        (count_divisible_3 + count_divisible_5)
    return count_total - count_complement


def main():
    # assert (calc_a31(1) == 0)
    # assert (calc_a31(2) == 0)
    # assert (calc_a31(3) == 1)
    # assert (calc_a31(10) == 5)
    # assert (calc_a31(30) == 14)
    # assert (calc_a31(100000000000) == 46666666667)

    n = int(input())
    print(calc_a31(n))


main()
