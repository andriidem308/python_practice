#include <iostream>
#include <algorithm>

using namespace std;

int n, m[1001];


int procedure(int nn, int visible){
	int first, second, best;

	switch (nn) {
		case 1:
			if (visible)
				printf("%d\n", m[0]);
			return m[0];
		case 2:
			if (visible)
				printf("%d %d\n", m[0], m[1]);
			return m[1];
		case 3:
			if (visible)
			{
				printf("%d %d\n", m[0], m[1]);
				printf("%d\n", m[0]);
				printf("%d %d\n", m[0], m[2]);
			}
			return m[0] + m[1] + m[2];
	}

	first = m[0] + 2*m[1] + m[nn-1];
	second = 2*m[0] + m[nn-2] + m[nn-1];

	if (first < second) best = first;
	else best = second;

	if (visible){
		if (best == first){
			printf("%d %d\n", m[0], m[1]);
			printf("%d\n", m[0]);
			printf("%d %d\n", m[nn - 2], m[nn - 1]);
			printf("%d\n", m[1]);
		} else {
			printf("%d %d\n", m[0], m[nn - 2]);
			printf("%d\n", m[0]);
			printf("%d %d\n", m[0], m[nn - 1]);
			printf("%d\n", m[0]);
		}
	}

	return best + procedure(nn - 2, visible);
}

int main() {
	while (scanf("%d", &n) == 1){
		for (int i = 0; i < n; i++) scanf("%d", &m[i]);

		sort(m, m + n);

		int res = procedure(n, 0);
		printf("%d\n", res);
		res = procedure(n, 1);
	}

	return 0;
}