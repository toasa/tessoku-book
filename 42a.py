class Student:
    def __init__(self, _id, tairyoku, kiryoku):
        self.id = _id
        self.tairyoku = tairyoku
        self.kiryoku = kiryoku

    def print(self):
        print("[{}] tai: {}, ki: {}".format(
            self.id, self.tairyoku, self.kiryoku))


def solve_a42(N, K, A, B):
    bunpu_tairyoku = [[] for _ in range(250)]
    bunpu_kiryoku = [[] for _ in range(250)]

    students = []
    for i in range(N):
        a = A[i]
        b = B[i]
        students.append(Student(i+1, a, b))

        bunpu_tairyoku[a].append(i+1)
        bunpu_kiryoku[b].append(i+1)

    students_orderd_by_tairyoku = sorted(students, key=lambda s: s.tairyoku)
    students_orderd_by_kiryoku = sorted(students, key=lambda s: s.kiryoku)

    res = 0

    for stu_tai in students_orderd_by_tairyoku:
        in_range_students_tai = []
        for cur_tai in range(stu_tai.tairyoku, stu_tai.tairyoku+K+1):
            if len(bunpu_tairyoku[cur_tai]) > 0:
                in_range_students_tai.extend(bunpu_tairyoku[cur_tai])

        # print("   in range:", in_range_students_tai)

        for stu_ki in students_orderd_by_kiryoku:
            in_range_students_ki = []
            for cur_ki in range(stu_ki.kiryoku, stu_ki.kiryoku+K+1):
                if len(bunpu_kiryoku[cur_ki]) > 0:
                    in_range_students_ki.extend(bunpu_kiryoku[cur_ki])

            res = max(len(set(in_range_students_tai) &
                          set(in_range_students_ki)), res)

    return res


def main():
    # assert (solve_a42(1, 30, [10], [30]) == 1)
    # assert (solve_a42(4, 30, [20, 10, 50, 30], [30, 40, 10, 60]) == 3)

    N, K = map(int, input().split())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(solve_a42(N, K, A, B))


main()
