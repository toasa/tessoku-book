class FordFulkerson:
    def __init__(self, n_node, edge_infos):
        self.n_node = n_node
        self.start = 1
        self.end = n_node

        self.flows = [[0 for _ in range(n_node+10)] for _ in range(n_node+10)]
        self.adjs = [[] for _ in range(n_node+10)]

        for src, dst, cap in edge_infos:
            self.flows[src][dst] = cap
            self.adjs[src].append(dst)
            self.adjs[dst].append(src)

    def __choose_path(self):
        stack = [self.start]
        visited = [False for _ in range(self.n_node+10)]
        visited[self.start] = True

        chosen_path = []

        while len(stack) > 0:
            src = stack.pop()
            chosen_path.append(src)

            if src == self.end:
                break

            cannot_flow = True

            for dst in self.adjs[src]:
                if not visited[dst] and self.flows[src][dst] > 0:
                    stack.append(dst)
                    visited[dst] = True
                    cannot_flow = False
                    break

            if cannot_flow:
                chosen_path.pop()
                stack = chosen_path

        path_len = len(chosen_path)
        if path_len == 0 or chosen_path[path_len-1] != self.end:
            return 0

        # Calculate minimum amount of flow
        amount = 2**64
        for i in range(path_len-1):
            src, dst = chosen_path[i], chosen_path[i+1]
            amount = min(amount, self.flows[src][dst])

        # Update residual path
        for i in range(path_len-1):
            src, dst = chosen_path[i], chosen_path[i+1]
            self.flows[src][dst] -= amount
            self.flows[dst][src] += amount

        return amount

    def solve(self):
        res = 0

        while True:
            amount = self.__choose_path()
            if amount == 0:
                break

            res += amount

        return res


def test1():
    ffa = FordFulkerson(
        6,
        [
            [1, 2, 5],
            [1, 3, 5],
            [2, 4, 4],
            [2, 3, 37],
            [3, 4, 3],
            [3, 5, 9],
            [4, 5, 56],
            [4, 6, 9],
            [5, 6, 2],
        ]
    )

    assert (ffa.solve() == 9)


def test2():
    ffa = FordFulkerson(
        6,
        [
            [1, 2, 5],
            [1, 4, 4],
            [2, 3, 4],
            [2, 5, 7],
            [3, 6, 3],
            [4, 5, 3],
            [5, 6, 5],
        ]
    )

    assert (ffa.solve() == 8)


test1()
test2()
