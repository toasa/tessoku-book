import math


def isPrime(x):
    if x <= 3:
        return True

    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False

    return True


def main():
    Q = int(input())
    X = []
    for _ in range(Q):
        X.append(int(input()))

    for x in X:
        print("Yes" if isPrime(x) else "No")


main()
