# WIP

LIMIT = 1000000007

a, b = map(int, input().split())
x = 1
for _ in range(b):
    x *= a
    if x >= LIMIT:
        x %= LIMIT

print(x)
