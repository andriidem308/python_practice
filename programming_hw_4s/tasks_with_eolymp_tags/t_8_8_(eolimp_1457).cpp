#include <iostream>
#include <vector>

using namespace std;

string analyze(vector<int> &arr, int arr_size, int p){
	int i, j;
	int tmp;

	for (i = 1; i < arr_size; i++){
		j = i;
		tmp = arr[i];

		while (j > 0 && arr[j - 1] > arr[j]){
			if (p < arr[j - 1] + tmp) return "No";
			arr[j] = arr[j - 1];
			j--;
		}

		arr[j] = tmp;
	}

	return "Yes";
}

int main(){
	int n, m;
	vector<int> cars;
	cin >> n >> m;
	cars.resize(n);
	for (int c = 0; c < n; c++) cin >> cars[c];

	cout << analyze(cars, n, m);
	return 0;
}