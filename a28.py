N = int(input())

x = 0
for _ in range(N):
    T, A = input().split()
    if T == '+':
        x += int(A)
    elif T == '-':
        x -= int(A)
    else:
        x *= int(A)
    # if x >= 10000:
    x %= 10000

    print(x)
