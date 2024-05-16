def solve_b43(n_student,  incorrect_answerers):
    n_quiz = len(incorrect_answerers)

    n_correct_answers = [n_quiz for _ in range(n_student+10)]
    for i in incorrect_answerers:
        n_correct_answers[i] -= 1

    return n_correct_answers[1:n_student+1]


def test():
    assert (
        solve_b43(1, [1])
        ==
        [0]
    )

    assert (
        solve_b43(4, [1, 4, 1, 4, 2, 1])
        ==
        [3, 5, 6, 4]
    )


def main():
    n_student, _ = map(int, input().split())
    incorrect_answerers = list(map(int, input().split()))

    res = solve_b43(n_student, incorrect_answerers)

    for r in res:
        print(r)


# test()
main()
