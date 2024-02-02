N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = [0, 0] + A
B = [0, 0, 0] + B

# dp[i] := 部屋 1 から部屋 i までの最短移動時間
dp = [0] * (N + 1)
dp[2] = A[2]

for i in range(3, N + 1):
    dp[i] = min(dp[i-1] + A[i], dp[i-2] + B[i])

print(dp[N])
