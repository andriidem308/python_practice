#include <iostream>
#include <string.h>

#define MAX_SIZE 2001
using namespace std;


char cur_line[MAX_SIZE];
int line_len, br_arr[MAX_SIZE][MAX_SIZE];

int calc_ways(int n, int k)
{
	if (k < 0) return 0;
	if (n == line_len) return (k == 0);
	if (br_arr[n][k] != -1) return br_arr[n][k];
	if (cur_line[n] == '(') return br_arr[n][k] = calc_ways(n + 1, k + 1);
	if (cur_line[n] == ')') return br_arr[n][k] = calc_ways(n + 1, k - 1);

	return br_arr[n][k] = (calc_ways(n + 1, k - 1) + calc_ways(n + 1, k + 1)) % 301907;
}

int main() {
	gets(cur_line);
	line_len = strlen(cur_line);

	memset(br_arr, -1, sizeof br_arr);
	printf("%d\n", calc_ways(0, 0));

	return 0;
}