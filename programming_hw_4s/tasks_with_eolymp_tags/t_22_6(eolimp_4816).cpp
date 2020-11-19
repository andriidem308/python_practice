#include <iostream>
#include <vector>

using namespace std;

vector<vector <int> > graph, result;
vector<int> vertices, result_w;

void dfs (int e) {
	vertices[e] = true;

	for (auto edge : graph[e])
		if (!vertices[edge]) dfs (edge);

	result_w.push_back(e);
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, m;
	cin >> n >> m;

	vertices.resize(n);
	graph.resize(n);

	for (int i = 0; i < m; i++){
		int v_1, v_2;
		cin >> v_1 >> v_2;

		v_1--;
		v_2--;

		graph[v_1].push_back(v_2);
		graph[v_2].push_back(v_1);
	}

	for (int i = 0; i < n; i++){
		if (!vertices[i]){
			dfs(i);

			result.push_back(result_w);
			result_w.clear();
		}
	}

	cout << result.size() << endl;

	for (auto edge : result){
		cout << edge.size() << endl;
		for (auto u : edge) cout << u + 1 << ' ';
		cout << endl;
	}

	return 0;
}