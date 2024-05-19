#include <iostream>
#include <set>
#include <tuple>
#include <vector>

using u64 = uint64_t;

void solve_b55() {
    std::set<u64> S;

    u64 Q;
    std::cin >> Q;

    std::vector<std::tuple<u64, u64>> queries;
    for (u64 i = 0; i < Q; i++) {
        u64 x, y;
        std::cin >> x >> y;
        queries.push_back({x, y});
    }

    for (u64 i = 0; i < Q; i++) {
        u64 x = std::get<0>(queries[i]);
        u64 y = std::get<1>(queries[i]);

        switch (x) {
        case 1:
            S.insert(y);
            break;
        case 2:
            if (S.size() == 0) {
                std::cout << -1 << std::endl;
                continue;
            }

            auto it = S.lower_bound(y); // y 以上の最小の値

            u64 dist_r;
            if (it == S.end())
                dist_r = 1000000000000000;
            else
                dist_r = *it - y;

            if (it != S.begin())
                it--;

            u64 dist_l = y - *it;

            std::cout << std::min(dist_l, dist_r) << std::endl;

            break;
        }
    }
}

int main() { solve_b55(); }