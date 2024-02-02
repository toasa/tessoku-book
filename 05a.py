N, K = map(int, input().split())

count = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if i + j >= K:
            break

        k = K - (i + j)
        if 1 <= k <= N:
            count += 1

print(count)
