#include <bits/stdc++.h>

using namespace std;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(nullptr);
	cout.tie(nullptr);

	set <pair<int,string>> priority_queue;
	map <string, int> node;

	string s;
	while (cin >> s){
		if (s[0] == 'A'){
			string id;
			int priority;

			cin >> id >> priority;

			priority_queue.insert({-priority, id});
			node[id] = priority;
		}

		if (s[0] == 'P'){
			cout << (*priority_queue.begin()).second << ' ' << -(*priority_queue.begin()).first << '\n';
			priority_queue.erase(priority_queue.begin());
		}

		if (s[0] == 'C'){
			string id;
			int new_priority;

			cin >> id >> new_priority;

			priority_queue.erase({-node[id], id});
			priority_queue.insert({-new_priority, id});
			node[id] = new_priority;
		}
	}

	return 0;
}
