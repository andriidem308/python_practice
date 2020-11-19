#include <iostream>

using namespace std;

int m, MOD = 1000003;

struct Math {
	long pow_mod(long a, long p) {
		if (a >= m) a %= MOD;
		if (a == 0) return 0;
		if (p == 0) return 1;

		long t = pow_mod(a, p / 2);
		if (p & 1) return a * t % MOD * t % MOD;

		return t*t % MOD;
	}

	long inverse(long a) { return pow_mod(a, MOD - 2); }
	long C_MOD(long n, long k) {
		long answer = 1;

		if (k > n / 2) k = n - k;

		for (int i = 1; i <= k; i++){
			answer *= n - k + i;
			answer %= MOD;
			answer *= inverse(i);
			answer %= MOD;
		}

		return answer;
	}
} math;

struct BST{
	struct node {
		int value, cur_size, FUN;
		node *ch[2];
	} * root;

	void Del(node* T) {
		if (!T) return;
		Del(T->ch[0]);
		Del(T->ch[1]);
		delete T;
	}

	void reset(){
		Del(root);
		root = nullptr;
	}

	int get_size(node *T) { return T ? T->cur_size : 0; }

	void insert(int v, node* &T){
		if (!T){
			T = new node();
			T->value = v;
			T->cur_size = 1;
		} else {
			insert(v, T->ch[v > T->value]);
			T->cur_size = get_size(T->ch[0]) + get_size(T->ch[1]) + 1;
		}
	}

	int fun(node* T){
		if (!T) return 1;
		if (T->FUN) return T->FUN;

		return T->FUN = (long) fun(T->ch[0]) * fun(T->ch[1]) % MOD \
 * math.C_MOD(get_size(T->ch[0]) + get_size(T->ch[1]), get_size(T->ch[0])) % MOD;
	}
} bst;

int main() {
	int T, n, A[1010];

	scanf("%d", &T);

	for (int case_n = 1; case_n <= T; case_n++){
		int i, j, result;
		scanf("%d%d", &n, &m);

		for (i = 1; i <= n; i++) scanf("%d", &A[i]);
		bst.reset();
		for (j = 1; j <= n; j++) bst.insert(A[j], bst.root);

		result = bst.fun(bst.root) * math.C_MOD(m, n) % MOD;
		printf("%d\n", result);
	}
}
