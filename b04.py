N = input()

n = 0
for i in range(len(N)):
    c = N[len(N) - i - 1]
    if c == '1':
        n += 2 ** i

print(n)
