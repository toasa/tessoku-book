def solve_b45(a, b, c):
    return "Yes" if a+b+c == 0 else "No"


def test():
    assert (solve_b45(3, -4, 1) == "Yes")
    assert (solve_b45(100, 0, 0) == "No")


def main():
    a, b, c = map(int, input().split())

    print(solve_b45(a, b, c))


# test()
main()
