#include <iostream>
#include <vector>

using namespace std;

int res[100010];
int num = 1;
vector <int> graph[100010], graph_top[100010];
vector <bool> used;
vector <int> order, component;

void dfs_a(int edge) {
	used[edge] = 1;
	for (int i = 0; i < graph[edge].size(); i++) {
		if (used[graph[edge][i]] == 0)
			dfs_a(graph[edge][i]);
	}

	order.push_back(edge);
}

void dfs_b(int edge) {
	used[edge] = 1;
	component.push_back(edge);

	for (int i = 0; i < graph_top[edge].size(); i++) {
		if (used[graph_top[edge][i]] == 0)
			dfs_b(graph_top[edge][i]);
	}
}

int main(){
	ios::sync_with_stdio(false);

	int n, m;
	cin >> n >> m;

	while (m--) {
		int a, b;
		cin >> a >> b;

		a--;
		b--;

		graph[a].push_back(b);
		graph_top[b].push_back(a);
	}

	used.assign(n, false);

	for (int i = 0; i < n; i++) {
		if (used[i] == 0)
			dfs_a(i);
	}

	used.assign(n, false);

	for (int i = 0; i < n; i++) {
		int v = order[n - 1 - i];
		if (used[v] == 0) {
			dfs_b(v);

			for (auto cmp = component.begin(); cmp != component.end(); cmp++) res[*cmp] = num;
			num++;

			component.clear();
		}
	}

	cout << num - 1 << endl;
	for (int i = 0; i < n - 1; i++) cout << res[i] << " ";
	cout << res[n - 1] << endl;

	return 0;
}
