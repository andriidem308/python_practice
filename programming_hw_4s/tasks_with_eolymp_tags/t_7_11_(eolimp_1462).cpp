#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int n;
	int val;
	vector<vector<int>> arr(10, vector<int>());
	vector<int> arr_sorted;

	cin >> n;
	for (int i = 0; i < n; i++){
		cin >> val;
		arr[val % 10].push_back(val);
	}

	for (int i = 0; i < 10; i++)
		sort(arr[i].begin(), arr[i].end());

	for (int i = 0; i < 10; i++)
		for (unsigned int j = 0; j < arr[i].size(); j++)
			arr_sorted.push_back(arr[i][j]);

	cout << arr_sorted[0];

	for (int i = 1; i < arr_sorted.size(); i++)
		cout << " " << arr_sorted[i];

	cout << "\n";

	return 0;
}
