# ニュートン・ラフソン法で解く
def solve_b12(N):
    def f(x): return x**3 + x - N
    def f1(x): return 3*(x**2) + 1

    # f は単調増加なので、ニュートン法のスタート地点はNの最大値で良いはず
    x = 10**5

    for i in range(50):
        # print("{}th: x: {:.6f}, f(x): {:.6f}".format(i, x, f(x)))
        x -= f(x)/f1(x)

    return x


def test():
    def f(x, N): return x**3 + x - N

    def check(N, ans):
        # Error must be less than 0.001
        assert f(ans, N) <= 0.001

    for N in range(1, 10**5+1):
        check(N, solve_b12(N))


def main():
    N = int(input())
    print(solve_b12(N))


# test()
main()
