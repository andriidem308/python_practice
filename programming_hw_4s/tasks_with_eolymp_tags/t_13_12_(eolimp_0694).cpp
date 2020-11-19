#include <stdio.h>

int x, i, n, a, b, c;
long result = 0;

class Deque{
public:
	int *value, *cur_min, front, back, front_m, back_m;

	Deque(int n = 1000010){
		value = new int[n];
		cur_min = new int[n];
		front = back = front_m = back_m = 0;
	}

	~Deque(){
		delete[] value;
		delete[] cur_min;
	}

	void pop(){
		if (front != back)
		{
			if (value[front] == cur_min[front_m]) front_m++;
			front++;
		}
	}

	int get_min() const {return front_m != back_m ? cur_min[front_m] : 0;}

	void push(int x){
		value[back++] = x;
		while (front_m != back_m && x < cur_min[back_m - 1]) back_m--;
		cur_min[back_m++] = x;
	}
};

int main(){
	scanf("%d %d %d %d %d", &n, &a, &b, &c, &x);
	Deque d(n);

	for (i = 1; i <= n; i++){
		x = (1L*a*x*x + 1L*b*x + c) / 100 % 1000000L;

		if (x % 5 < 2) d.pop();
		else d.push(x);

		result += d.get_min();
	}

	printf("%ld\n", result);

	return 0;
}