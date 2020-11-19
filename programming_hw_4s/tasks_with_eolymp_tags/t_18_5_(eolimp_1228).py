#include <bits/stdc++.h>

using namespace std;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int n;
	multiset <long long> s;
	long long result = 0;

	cin >> n;

	for (int i = 0; i < n; i++){
		long long x;
		cin >> x;
		s.insert(x);
	}

	while (s.size() > 1){
		long long value_1 = *s.begin(); s.erase(s.begin());
		long long value_2 = *s.begin(); s.erase(s.begin());

		s.insert(value_1 + value_2);
		result += value_1 + value_2;
	}

	cout << result << endl;

	return 0;
}