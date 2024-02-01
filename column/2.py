N = int(input())
A = list(map(int, input().split()))
S = int(input())

count = 0

for selection_mask in range(1 << N):
    total = 0
    for i in range(N):
        if (1 << i) & selection_mask == (1 << i):
            total += A[i]
            # print("{}th card selected!".format(i))

    if total == S:
        count += 1

print(count)
