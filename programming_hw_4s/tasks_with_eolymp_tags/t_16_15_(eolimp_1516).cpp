#include <iostream>
#include <cmath>
#include <algorithm>


using namespace std;


void build_tree(int n1, int n2, int h) {
	int n = n2 - n1 + 1;

	if ((n == 0) || (h == 0)) return ;

	int h_pow = pow(2, h);

	if((n > 1) || (h > 1)) {
		if(n > (h_pow - 1)) {
			printf(" Impossible.");
			return;
		}
	}

	int to_left = max(n - h_pow / 2, 0);

	printf(" %d", n1 + to_left);
	if(to_left > 0) build_tree(n1, n1 + to_left - 1, h - 1);
	build_tree(n1 + to_left + 1, n2, h - 1);
}

int main() {
	int n, h, case_number = 0;

	do {
		case_number++;
		scanf("%d %d", &n, &h);

		if(n == 0) break;

		printf("Case %d:", case_number);
		build_tree(1, n, h);
		printf("\n");
	} while(true);

	return 0;
}
