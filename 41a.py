def solve_a41(S):
    N = len(S)
    i = 0
    while i+2 < N:
        if S[i] == S[i+1] == S[i+2]:
            return "Yes"
        elif S[i] == S[i+1]:
            i += 2
        else:
            i += 1

    return "No"


def main():
    # assert (solve_a41("BBB") == "Yes")
    # assert (solve_a41("BRB") == "No")
    # assert (solve_a41("BBR") == "No")
    # assert (solve_a41("BBBB") == "Yes")
    # assert (solve_a41("BBBR") == "Yes")
    # assert (solve_a41("BBRR") == "No")
    # assert (solve_a41("BBRR") == "No")
    # assert (solve_a41("BBBRR") == "Yes")
    # assert (solve_a41("BBRRR") == "Yes")
    # assert (solve_a41("RBBRRR") == "Yes")
    # assert (solve_a41("BBRRRBB") == "Yes")
    # assert (solve_a41("BRBBBRB") == "Yes")
    # assert (solve_a41("BRBRBRB") == "No")

    _ = input()
    S = input()
    print(solve_a41(S))


main()
