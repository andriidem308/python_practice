#include <iostream>
#include <vector>
#include <set>

using namespace std;

struct vertex {
	int used, color;
	vector<int> g, gr;
};

vector <int> graph;
vector <vertex> vertices;

void dfs(int v) {
	vertices[v].used = 1;

	for (int i = 0; i < vertices[v].g.size(); i++) {
		int to = vertices[v].g[i];
		if (!vertices[to].used) dfs(to);
	}

	graph.push_back(v);
}

void dfs_r(int v, int c) {
	vertices[v].used = 2;
	vertices[v].color = c;

	for (int i = 0; i < vertices[v].gr.size(); i++) {
		int to = vertices[v].gr[i];
		if (vertices[to].used != 2) dfs_r(to, c);
	}
}

int main() {
	int n, m;
	int color = 0;

	cin >> n >> m;

	vertices.resize(n);

	while (m--) {
		int a, b;
		cin >> a >> b;

		vertices[a - 1].g.push_back(b - 1);
		vertices[b - 1].gr.push_back(a - 1);
	}

	for (int i = 0; i < n; i++) {
		if (!vertices[i].used)
			dfs(i);
	}

	for (int i = graph.size() - 1; i >= 0; i--) {
		if (vertices[graph[i]].used != 2)
			dfs_r(graph[i], color++);
	}

	set <int> gg[10000];

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < vertices[i].g.size(); j++)
			if (vertices[i].color != vertices[vertices[i].g[j]].color)
				gg[vertices[i].color].insert(vertices[vertices[i].g[j]].color);
	}

	int result = 0;
	for (int i = 0; i < 10000; i++) result += gg[i].size();

	cout << result << endl;
}
