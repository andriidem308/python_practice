#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


void swap_values(int &a, int &b)
{
	int tmp = a;
	a = b;
	b = tmp;
};

int main()
{
	int n;
	vector<int> arr;

	int result = 0;

	cin >> n;
	arr.resize(n);

	for (int i = 0; i < n; i++)
		cin >> arr[i];

	int first = arr[0];

	for (int i = 0; i < n; i ++){
		int minx = i;

		for (int j = i + 1; j < n; j++){
			if (arr[minx] > arr[j])
				minx = j;
		}

		if (minx != i){
			if (arr[i] == first || arr[minx] == first)
				result++;
		}

		swap_values(arr[minx], arr[i]);
	}

	cout << result;
	return 0;
}
