A, B = map(int, input().split())


def main():
    for i in range(A, B+1):
        if 100 % i == 0:
            print("Yes")
            return
    print("No")


main()
