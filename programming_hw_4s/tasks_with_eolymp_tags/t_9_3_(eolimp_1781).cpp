#include <iostream>
#include <algorithm>

using namespace std;

int calculate_permutation(int n, int lst_a[11][11]){
	int lst_b[11];
	int min_sum = 10000000;

	for (int i = 0; i < n; ++i) 
		lst_b[i] = i;

	do{
		int sum = 0;
		
		for (int worker = 0; worker < n; ++worker)
			sum += lst_a[worker][lst_b[worker]];

		min_sum = min(min_sum, sum);
	}
	while (next_permutation(lst_b, lst_b + n));

	return min_sum;
}

int main() {
	int n;
	int salaries[11][11];
	
	cin >> n;

	for (int i = 0; i < n; ++i){
		for (int j = 0; j < n; ++j) 
			cin >> salaries[i][j];
	}

	cout << calculate_permutation(n, salaries);

	return 0;
}
