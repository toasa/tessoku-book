def solve_a44(N, Qs):
    A = [i for i in range(1, N+1)]

    is_reverse = False

    for Q in Qs:
        # if is_reverse:
        #     print("===", list(reversed(A)))
        # else:
        #     print("===", A)

        if Q[0] == 1:
            # Set
            idx = -1*Q[1] if is_reverse else Q[1]-1
            n = Q[2]
            A[idx] = n

        elif Q[0] == 2:
            # Reverse
            is_reverse = not is_reverse

        else:
            # Get
            idx = -1*Q[1] if is_reverse else Q[1]-1
            print(A[idx])


def main():
    # solve_a44(5, [[1, 4, 8], [3, 2], [2], [3, 2]])

    N, Q = map(int, input().split())
    Qs = []
    for _ in range(Q):
        q = list(map(int, input().split()))
        Qs.append(q)
    solve_a44(N, Qs)


main()
