#include <iostream>
#include <string>

using namespace std;

struct deque{
	int data[1000];
	int end = 0, dsize = 0, start = 1, lol = 100;

	int push_back(int x){
		end = (end + 1) % lol;
		data[end] = x;
		dsize++;
	}

	int push_front(int x){
		start = (start - 1 + lol) % lol;
		data[start] = x;
		dsize++;
	}

	void pop_back(){
		end = (end - 1 + lol) % lol;
		dsize--;
	}

	void pop_front(){
		start = (start + 1) % lol;
		dsize--;
	}

	int back() const{ return data[end]; }
	int size() const{ return dsize; }

	void clear(){
		end = 0;
		dsize = 0;
		start = 1;
	}

	int front() const{ return data[start]; }
};

int main() {
	deque new_deque;
	string cmd;
	int n;

	while (cin >> cmd){
		if (cmd == "push_back"){
			cin >> n;
			new_deque.push_back(n);
			cout << "ok\n";
		}
		else if (cmd == "push_front"){
			cin >> n;
			new_deque.push_front(n);
			cout << "ok\n";
		}
		else if (cmd == "pop_back"){
			if (new_deque.size()){
				cout << new_deque.back() << endl;
				new_deque.pop_back();
			}
			else cout << "error\n";
		}
		else if (cmd == "pop_front"){
			if (new_deque.size()){
				cout << new_deque.front() << endl;
				new_deque.pop_front();
			}
			else cout << "error\n";
		}
		else if (cmd == "front"){
			if (new_deque.size()) cout << new_deque.front() << endl;
			else cout << "error\n";
		}
		else if (cmd == "back"){
			if (new_deque.size()) cout << new_deque.back() << endl;
			else cout << "error\n";
		}
		else if (cmd == "size") cout << new_deque.size() << endl;
		else if (cmd == "clear"){
			new_deque.clear();
			cout << "ok\n";
		}
		else if (cmd == "exit"){
			cout << "bye\n";
			return 0;
		}
	}
	return 0;
}