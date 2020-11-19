#include <iostream>


using namespace std;

const int MOD = 786433;
const int PHI = 1 << 18;
const int MAX_N = 1 << 16;

int f[2][MAX_N], res[MAX_N];
int mpos = 0, mem[MAX_N * 4];


inline int mul(int a, int b ) { return ((long long)a * b) % MOD; }

int pow(int a, int n){
	if (n == 1) return a;
	int x = pow(a, n >> 1);
	x = mul(x, x);

	return (n & 1) ? mul(x, a) : x;
}

int inv(int x){ return pow(x, MOD - 2);}

void FFT(int len, int * result, int * a, int x){
	if (len == 1){ result[0] = a[0]; return; }

	int l = len / 2;
	int * a0 = mem + mpos; mpos += l;
	int * a1 = mem + mpos; mpos += l;

	for (int i = 0; i < l; i++){
		a0[i] = a[i + i];
		a1[i] = a[i + i + 1];
	}

	int * r0 = mem + mpos; mpos += l;
	int * r1 = mem + mpos; mpos += l;
	int t = 1, tmp;

	FFT(l, r0, a0, mul(x, x));
	FFT(l, r1, a1, mul(x, x));

	for (int i = 0; i < l; i++){
		tmp = mul(t, r1[i]);

		if ((result[i] = r0[i] + tmp) >= MOD) result[i] -= MOD;
		if ((result[i + l] = r0[i] - tmp) < 0) result[i + l] += MOD;

		t = mul(t, x);
	}

	mpos -= 2 * len;
}

int main(){
	int n, h;
	cin >> n >> h;

	h++;
	int N = 1 << h;
	int x = pow(5, PHI / N);

	for (int i = 0; i < N; i++) f[0][i] = 1;
	f[1][0] = 1;
	for (int i = 1; i < N; i++) f[1][i] = mul(f[1][i - 1], x);

	for (int k = 2; k <= h; k++)
		for (int t = 1, i = 0; i < N; i++)
			f[k & 1][i] = (long long) f[(k & 1) ^ 1][i] * (f[(k & 1) ^ 1][i] + 2 * f[k & 1][i]) * t % MOD, t = mul(t, x);

	FFT(N, res, f[h & 1], inv(x));

	cout << mul(res[n], inv(N)) << endl;
}