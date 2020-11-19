#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>

using namespace std;

struct Node{
	int min;
	int add;
}
seg_tree[1 << 18];

void build(vector<int> &a, int v, int pos_l, int pos_r)
{
	if (pos_l == pos_r){
		seg_tree[v].min = a[pos_l];
		seg_tree[v].add = 0;
	}

	if (pos_l != pos_r) {
		int middle = (pos_l + pos_r) / 2;

		build(a, v*2, pos_l, middle);
		build(a, v*2 + 1, middle + 1, pos_r);

		seg_tree[v].min = min(seg_tree[v*2].min, seg_tree[v*2 + 1].min);
		seg_tree[v].add = 0;
	}
}

void push(int v){
	if (seg_tree[v].add){
		seg_tree[2*v].add += seg_tree[v].add;
		seg_tree[2*v].min += seg_tree[v].add;
		seg_tree[2*v + 1].add += seg_tree[v].add;
		seg_tree[2*v + 1].min += seg_tree[v].add;
		seg_tree[v].add = 0;
	}
}

void add_value(int v, int pos_l, int pos_r, int left, int right, int value){
	if (left > right) return;

	if (pos_l == left && pos_r == right){
		seg_tree[v].add += value;
		seg_tree[v].min += value;
		return;
	}

	int middle = (pos_l + pos_r) / 2;
	push(v);
	add_value(2*v, pos_l, middle, left, min(middle, right), value);
	add_value(2*v + 1, middle + 1, pos_r, max(left, middle + 1), right, value);
	seg_tree[v].min = min(seg_tree[2*v].min, seg_tree[2*v + 1].min);
}

int main(){
	char s[100001];

	int n;
	int k, p, sum_v;
	vector<int> v;

	gets(s);
	n = strlen(s);

	for (int i = sum_v = 0; i < n; i++){
		s[i] == '(' ? sum_v++ : sum_v--;
		v.push_back(sum_v);
	}

	build(v, 1, 0, n - 1);
	scanf("%d", &k);

	while (k--){
		scanf("%d", &p);
		if (s[p] == '('){
			s[p] = ')';
			add_value(1, 0, n - 1, p, n - 1, -2);
			sum_v -= 2;
		}

		if (s[p] != '('){
			s[p] = '(';
			add_value(1, 0, n - 1, p, n - 1, 2);
			sum_v += 2;
		}

		if (seg_tree[1].min >= 0 && sum_v == 0) printf("+\n");
		else printf("-\n");
	}

	return 0;
}