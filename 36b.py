def is_even(n):
    return n % 2 == 0


def solve_b36(light_bulbs, n_on):
    on_count = 0
    for c in light_bulbs:
        if c == "1":
            on_count += 1

    if is_even(on_count) == is_even(n_on):
        return "Yes"
    else:
        return "No"


def test():
    assert (
        solve_b36("1010111", 3)
        ==
        "Yes"
    )

    assert (
        solve_b36("0001010001", 6)
        ==
        "No"
    )

    assert (
        solve_b36("11", 2)
        ==
        "Yes"
    )


def main():
    _, n_on = map(int, input().split())
    light_bulbs = input()

    print(solve_b36(light_bulbs, n_on))


# test()
main()
