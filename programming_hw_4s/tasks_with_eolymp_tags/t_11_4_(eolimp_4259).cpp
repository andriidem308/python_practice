#include <iostream>
#include <algorithm>

using namespace std;

class Stack {
public:
	Stack(int size);
	void push(int x);
	void pop();
	int get_min() const;
private:
	int* stack, size;
};

Stack::Stack(int size = 1000001) {
	stack = new int[size];
	this->size = 0;
}

void Stack::push(int x) {
	if (size == 0) stack[size++] = x;
	else{
		int pos = size - 1;
		stack[size++] = min(x, stack[pos]);
	}
}

void Stack::pop() { size--; }

int Stack::get_min() const { return stack[size - 1]; }



int main() {
	int n, x, op;
	scanf("%d", &n);

	Stack new_stack;
	while (n--){
		scanf("%d", &op);
		if (op == 1){
			scanf("%d", &x);
			new_stack.push(x);
		}
		else{
			if (op == 2) new_stack.pop();
			else printf("%d\n", new_stack.get_min());
		}
	}

	return 0;
}
