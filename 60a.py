class Price:
    def __init__(self, price, day):
        self.price = price
        self.day = day


def solve_a60(stock_pricies):
    stack = []
    res = []
    for d, p in enumerate(stock_pricies):
        while True:
            if len(stack) == 0:
                res.append(-1)
                stack.append(Price(p, d+1))
                break

            top = stack[len(stack)-1]
            if top.price > p:
                res.append(top.day)
                stack.append(Price(p, d+1))
                break

            stack.pop()

    print(*res)


def main():
    # assert (solve_a60([6, 2, 5, 3, 1, 4]) == "-1 1 1 3 4 3")

    _ = input()
    prices = list(map(int, input().split()))
    solve_a60(prices)


main()
