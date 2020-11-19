#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n;
    int a, b;
    int result;

    vector<int> arr;

	while (scanf("%d", &n) == 1){
		arr.resize(n);
		result = 0;

		for (int i = 0; i < n; i++)
		    scanf("%d", &arr[i]);
		scanf("%d %d", &a, &b);

		for (int i = 0; i < n; i++)
			if (arr[i] >= a && arr[i] <= b)
			    result++;

		printf("%d\n", result);
	}

	return 0;
}
