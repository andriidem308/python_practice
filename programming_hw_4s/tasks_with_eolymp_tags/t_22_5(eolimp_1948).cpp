#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool sorted = true;
vector<vector<int>> graph;
vector<int> vertices_first, vertices_second, result;

void dfs (int e) {
	vertices_first[e] = vertices_second[e] = true;

	for (auto edge : graph[e])
		if (!vertices_first[edge]) dfs (edge);
        else if (vertices_second[edge]) sorted = false;

	vertices_second[e] = false;
	result.push_back(e);
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m;
    cin >> n >> m;

    vertices_first.resize(n);
    vertices_second.resize(n);

    graph.resize(n);

    for (int i = 0; i < m; i++) {
        int v_1, v_2;
        cin >> v_1 >> v_2;

        v_1--;
        v_2--;

        graph[v_1].push_back(v_2);
    }

    for (int i = 0; i < n; i++) if (!vertices_first[i]) dfs(i);
    reverse(result.begin(), result.end());

    if (!sorted){ cout << "-1\n"; return 0; }
    for (int i = 0; i < n; i++) cout << result[i] + 1 << ' ';

    return 0;
}