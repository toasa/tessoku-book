#include <iostream>
#include <set>
#include <tuple>
#include <vector>

using u64 = uint64_t;

// g++ -std=c++11 55a.cc && ./a.out

void solve_a55() {
    std::set<u64> S;

    std::vector<std::tuple<u64, u64>> queries;

    u64 Q;
    std::cin >> Q;

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
            S.erase(y);
            break;
        case 3:
            auto it = S.lower_bound(y);
            if (it == S.end())
                std::cout << -1 << std::endl;
            else
                std::cout << *it << std::endl;
            break;
        }
    }
}

int main() { solve_a55(); }