N = int(input())

P, A = [], []
for _ in range(N):
    p, a = map(int, input().split())
    P.append(p)
    A.append(a)

P = [0] + P
A = [0] + A

# dp[l][r]: l 番目から r 番目までのブロックが残っているような状態を考える。
# この状態になるまでに、最大何点を稼ぐことができるか。ただし、特典は
# ブロックが取り除かれたときに加算されるものとする。
dp = [[0] * (N+1) for _ in range(N+1)]
for l in range(1, N+1):
    for r in range(N, l-1, -1):
        scoreL = 0
        if 



