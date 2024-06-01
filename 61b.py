def solve_b61(n_student, A, B):
    student_memo = [set() for _ in range(n_student+10)]
    for a, b in zip(A, B):
        student_memo[a].add(b)
        student_memo[b].add(a)

    cur_max = -1
    cur_res = -1
    for i, s in enumerate(student_memo):
        if cur_max < len(s):
            cur_res = i
            cur_max = len(s)

    return cur_res


def main():
    n_student, n_relation = map(int, input().split())
    A, B = [], []
    for _ in range(n_relation):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    print(solve_b61(n_student, A, B))


main()
