import random
import math

LIMIT = 10000


class City:
    def __init__(self, _id, x, y):
        self.id = _id
        self.x = x
        self.y = y


def calc_total_distance(N, cities):
    total = 0
    for i in range(N):
        total += math.sqrt((cities[i].x-cities[i+1].x)
                           ** 2 + (cities[i].y-cities[i+1].y)**2)

    return total


def solve_a46(N, Xs, Ys):
    city1 = City(1, Xs[0], Ys[0])
    cities = []
    for i in range(1, N):
        cities.append(City(i+1, Xs[i], Ys[i]))

    res_min = 2 ** 64
    res_cities = None

    for _ in range(LIMIT):
        random.shuffle(cities)
        cur_cities = [city1]+cities+[city1]
        cur_distance = calc_total_distance(N, cur_cities)
        if cur_distance < res_min:
            res_min = cur_distance
            res_cities = cur_cities

    for c in res_cities:
        print(c.id)


def main():
    N = int(input())
    Xs, Ys = [], []
    for _ in range(N):
        x, y = map(int, input().split())
        Xs.append(x)
        Ys.append(y)

    solve_a46(N, Xs, Ys)


main()
