#include <iostream>
#include <string.h>

using namespace std;

int a, b, c, d, i, len, start;
char s[10001];

int main() {
	gets(s + 4); len = strlen(s + 4);

	start = (len % 4) ? len % 4 : 4;
	for (i = start; i < 4; i++) s[i] = '0';

	for (i = start; i <= len; i += 4)
	{
		sscanf(s + i, "%1d%1d%1d%1d", &a, &b, &c, &d);
		printf("%X", 8*a + 4*b + 2*c + d);
	}
	printf("\n");
	return 0;
}