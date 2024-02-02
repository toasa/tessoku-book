N = int(input())

for i in range(9, -1, -1):
    on = N // (2 ** i) == 1
    print("1" if on else "0", end="")
    N %= (2 ** i)

print()
