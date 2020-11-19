#include<iostream>
#include<vector>
#include<math.h>

using namespace std;
double find_distance(int x0, int y0, int x1, int y1){
	int a = (x1-x0);
	int b = (y1-y0);

	return sqrt(a*a + b*b);
}

int main(){
	int n, r;
	vector<int> x_arr, y_arr;
	scanf("%d %d", &n, &r);
	x_arr.resize(n);
	y_arr.resize(n);

	for (int i = 0; i < n; i++){
		scanf("%d %d", &x_arr[i], &y_arr[i]);
	}

	int res = 0;
	for (int i = 0; i < n; i++) {
		for (int j = i+1; j < n; j++) {
			int tx0 = x_arr[i], ty0 = y_arr[i];
			int tx1 = x_arr[j], ty1 = y_arr[j];

			if (find_distance(tx0, ty0, tx1, ty1) <= r) res++;
		}
	}

	printf("%d", res);

	return 0;
}
