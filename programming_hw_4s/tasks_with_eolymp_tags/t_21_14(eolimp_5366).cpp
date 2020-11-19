#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<vector<int> > g;
int a, b, i, n, ans_0, ans_1;

int dfs(int v, int p = -1){
	int i, res = 1;

	for (i = 0; i < g[v].size(); i++){
		int to = g[v][i];

		if (to == p) continue;
		res += dfs(to, v);
	}

	if (ans_0 == 0 && res >= n / 2 + 1) ans_0 = v;
	if (res * 2 == n) ans_1 = v;

	return res;
}

int main() {
	scanf("%d", &n);
	g.resize(n + 1);

	for (i = 0; i < n - 1; i++){
		scanf("%d %d", &a, &b);
		g[a].push_back(b);
		g[b].push_back(a);
	}

	ans_1 = ans_0 = 0;
	dfs(1);
	if (ans_1) printf("%d %d\n", min(ans_0, ans_1), max(ans_0, ans_1));
	else printf("%d\n", ans_0);

	return 0;
}
