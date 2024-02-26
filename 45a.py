def count_color(cards):
    count_r = 0
    count_b = 0
    count_w = 0
    for card in cards:
        if card == "R":
            count_r += 1
        elif card == "B":
            count_b += 1
        else:
            count_w += 1

    return count_r, count_b, count_w


# 仮説1. どんな2枚のカードの選び方をしても最終的なカードは変わらない
def solve_a45(cards, target):
    count_r, count_b, count_w = count_color(cards)

    if count_b == count_r:
        final_color = "W"
    elif count_b > count_r:
        if (count_b - count_r) % 3 == 0:
            final_color = "W"
        elif (count_b - count_r) % 3 == 1:
            final_color = "B"
        else:
            final_color = "R"
    else:
        if (count_r - count_b) % 3 == 0:
            final_color = "W"
        elif (count_r - count_b) % 3 == 1:
            final_color = "R"
        else:
            final_color = "B"

    return "Yes" if final_color == target else "No"


def main():
    # assert (solve_a45("BB", "B") == "No")
    # assert (solve_a45("BBB", "B") == "No")
    # assert (solve_a45("BBBB", "B") == "Yes")
    # assert (solve_a45("RR", "B") == "Yes")
    # assert (solve_a45("WBBR", "B") == "Yes")

    N, C = input().split()
    A = input()
    print(solve_a45(A, C))


main()
