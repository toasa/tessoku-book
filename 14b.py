def exhaustive_sum_list(arr):
    l = []

    for n in range(2**len(arr)):
        sum = 0
        for i in range(len(arr)):
            if n & 1 << i == 1 << i:
                sum += arr[i]
        l.append(sum)

    return l


def bisect(needle, haystack):
    l = -1
    r = len(haystack)

    while r-l > 1:
        mid = (l+r)//2
        if needle <= haystack[mid]:
            r = mid
        else:
            l = mid

    return r < len(haystack) and haystack[r] == needle


def solve_b14(ints, target_int):
    half_1st = ints[:len(ints)//2]
    half_2nd = ints[len(ints)//2:]

    ex1 = exhaustive_sum_list(half_1st)
    ex2 = exhaustive_sum_list(half_2nd)

    ex2.sort()
    for x in ex1:
        if x > target_int:
            continue
        elif x == target_int:
            return "Yes"
        else:
            if bisect(target_int-x, ex2):
                return "Yes"

    return "No"


def test():
    assert (
        solve_b14([5, 1, 18, 7, 2, 9], 30)
        ==
        "Yes"
    )


def main():
    _, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve_b14(A, K))


# test()
main()
