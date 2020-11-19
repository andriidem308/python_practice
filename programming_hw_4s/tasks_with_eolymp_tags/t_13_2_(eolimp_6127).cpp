#include <iostream>
#include <string>
using namespace std;

struct Node{
	Node * prev;
	int x;
	Node() { prev = nullptr; x = 0;}
	Node(Node * a, int b) { prev = a; x = b; }
};

struct queue{
private:
	Node * head = nullptr;
	Node * tail = nullptr;
	int count = 0;
public:
	int size() {
		return count;
	}

	void push(int p){
		if(count == 0){
			Node * NewNode = new Node(tail, p);

			head = NewNode;
			tail = NewNode;
		}
		else{
			Node * NewNode = new Node(nullptr, p);

			tail->prev = NewNode;
			tail = NewNode;
		}

		count++;
	}

	int front(){
		if(count) { return head->x; }
		return 0;
	}

	int pop(){
		if(count){
			int x = head->x;
			Node * NewNode = head->prev;

			delete head;

			head = NewNode;
			count--;

			return x;
		}
		return 0;
	}

	void clear(){
		while(count > 0){
			Node * NewNode = head->prev;

			delete head;

			head = NewNode;
			count--;
		}
		head = nullptr; tail = nullptr;
	}
};

int main() {
	queue new_queue;

	while(true){
		string s;
		cin >> s;

		if(s == "exit") {
			cout << "bye\n";
			break;
		}
		else if(s == "push"){
			int inp; cin >> inp; new_queue.push(inp); cout << "ok\n";
		}
		else if(s == "front"){
			if(new_queue.size()) cout << new_queue.front() << endl;
			else cout << "error\n";
		}
		else if(s == "size") {
			cout << new_queue.size() << endl;
		}
		else if(s == "pop"){
			if(new_queue.size()) cout << new_queue.pop() << endl;
			else cout << "error\n";
		}
		else if(s == "clear") {
			cout << "ok\n";
			new_queue.clear();
		}
	}
	return 0;
}