#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;

long op;


void merge(int *arr, int lf, int ll, int rf, int rl){
	int index_c = 0;
	int	left_bound = lf;
	int	length_current = rl - lf + 1;
	int *res = new int[length_current];

	while (lf <= ll && rf <= rl)
		if (arr[lf] <= arr[rf]) res[index_c++] = arr[lf++];
		else{
			res[index_c++] = arr[rf++];
			op += ll - lf + 1;
		}

	while (lf <= ll) res[index_c++] = arr[lf++];
	while (rf <= rl) res[index_c++] = arr[rf++];

	memcpy(arr + left_bound, res, length_current * sizeof(int));

	delete[] res;
}

void mergeSort(int *array, int index_l, int index_r){
	if (index_l >= index_r) return;

	int middle = (index_l + index_r) / 2;

	mergeSort(array, index_l, middle);
	mergeSort(array, middle + 1, index_r);
	merge(array, index_l, middle, middle + 1, index_r);
}

int main(){
	int n;
	int *current_arr;

	int i;

	while (scanf("%d", &n), n){
		current_arr = new int[n];
		for (op = i = 0; i < n; i++) scanf("%d", &current_arr[i]);

		mergeSort(current_arr, 0, n - 1);
		delete[] current_arr;

		printf("%ld\n", op);
	}

	return 0;
}
