#include <iostream>
#include <string.h>

using namespace std;

int t, swaps, m[50001];


void merge(int *a, int bleft, int bright, int cleft, int cright)
{
	const int len = bright - bleft + 1;
	int resCur = 0, q = 0, *res = new int[len];
	memcpy(res, a + bleft, len * sizeof(int));
	while (resCur < len && cleft <= cright)
	{
		while (res[q] <= a[cleft] + t && q < len) q++;
		if (res[resCur] <= a[cleft]) a[bleft++] = res[resCur++];
		else a[bleft++] = a[cleft++], swaps += len - q;
	}
	while (resCur < len) a[bleft++] = res[resCur++];
	delete[] res;
}


void merge_sort(int *a, int left, int right)
{
	if (left >= right) return;

	const int middle = (left + right) / 2;

	merge_sort(a, left, middle);
	merge_sort(a, middle + 1, right);
	merge(a, left, middle, middle + 1, right);
}

int main() {
	int i, n;

	scanf("%d %d", &n, &t);
	for (swaps = i = 0; i < n; i++) scanf("%d", &m[i]);

	merge_sort(m, 0, n - 1);

	printf("%d\n", swaps);
	return 0;
}