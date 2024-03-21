#include <iostream>
#include <vector>

using u64 = uint64_t;

class UnionFinder {
  public:
    UnionFinder(u64 n_node) {
        std::vector<Node> _nodes;

        for (u64 i = 0; i <= n_node; i++)
            _nodes.push_back(Node(i));

        nodes = _nodes;
    }

    void unite(u64 id1, u64 id2) {
        Node *r1 = root(id1);
        Node *r2 = root(id2);

        r1->parent = r2;
    }

    bool is_connected(u64 id1, u64 id2) {
        Node *r1 = root(id1);
        Node *r2 = root(id2);

        return r1->id == r2->id;
    }

  private:
    class Node {
      public:
        Node(u64 id) : id(id), parent(nullptr) {}

        u64 id;
        Node *parent;
    };

    Node *root(u64 id) {
        Node *cur = &nodes[id];
        if (cur->parent == nullptr)
            return cur;

        cur->parent = root(cur->parent->id);
        return cur->parent;
    }

    std::vector<Node> nodes;
};

using query = std::vector<u64>;

void solve_a66(uint64_t N, std::vector<query> &queries) {
    UnionFinder uf = UnionFinder(N);

    for (u64 i = 0; i < queries.size(); i++) {
        u64 id1 = queries[i][1];
        u64 id2 = queries[i][2];

        if (queries[i][0] == 1) {
            uf.unite(id1, id2);
        } else {
            bool b = uf.is_connected(id1, id2);
            printf("%s\n", b ? "Yes" : "No");
        }
    }
}

int main() {
    u64 N, Q;
    std::vector<query> queries;

    std::cin >> N >> Q;
    for (u64 i = 0; i < Q; i++) {
        u64 q, n1, n2;
        std::cin >> q >> n1 >> n2;
        queries.push_back({q, n1, n2});
    }

    solve_a66(N, queries);
}