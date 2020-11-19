#include<iostream>
#include<cstring>

using namespace std;

#define MAX 71
int m[MAX][MAX];

int main(){
	int n, t, p;
	int tests;
	memset(m,0,sizeof(m));

	for(int i = 0; i < MAX; i++) m[1][i] = m[i][0] = 1;
	for(int i = 2; i < MAX; i++)
		for(int j = 1; j < MAX; j++)
			m[i][j] = m[i][j-1] + m[i-1][j];


	scanf("%d",&tests);
	while(tests--){
		scanf("%d %d %d",&n,&t,&p);
		t -= n * p;
		printf("%d\n",m[n][t]);
	}
	return 0;
}