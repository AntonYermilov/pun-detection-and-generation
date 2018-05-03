#include <iostream>
#include <vector>

const int MAXN = 50000;

int n, m;
std::vector<int> g[MAXN];
int q[MAXN];
uint16_t d[MAXN];

void bfs(int from) {
    memset(d, -1, sizeof d);
    int front = 0, back = 0;
    d[from] = 0;
    q[back++] = from;

    while (front != back) {
        int v = q[front++];
        for (int u : g[v]) {
            if (d[u] == uint16_t(-1)) {
                d[u] = d[v] + 1;
                q[back++] = u;
            }
        }
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    std::freopen("tools/graph.txt", "r", stdin);

    std::cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int v, u;
        std::cin >> v >> u;
        v--, u--;
        g[v].push_back(u);
        g[u].push_back(v);
    }
    

    FILE *fp;
    fp = fopen("tools/distances.txt", "w");

    std::cout << "Calculation started" << std::endl;
    for (int v = 0; v < n; v++) {
        bfs(v);
        fwrite(d, sizeof(uint16_t), n, fp);
        if ((v + 1) % 500 == 0)
            std::cout << (v + 1) << "/" << n << " iteration done" << std::endl;
    }

    fclose(fp);
    return 0;
}
