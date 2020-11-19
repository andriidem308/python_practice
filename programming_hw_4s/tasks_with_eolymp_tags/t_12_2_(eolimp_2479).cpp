#include <iostream>
#include <string>
#include <stack>

#define pass (void)0

using namespace std;

int n;
string plain_text;


string check_brackets(){
	if (plain_text.empty()) return "Yes";

	stack<bool> brackets;

	for (char chr : plain_text){
		switch (chr) {
			case '(':
			{
				brackets.push(true);
				break;
			}
			case ')':
			{
				if (brackets.empty()) return "No";
				if (!brackets.top()) return "No";
				brackets.pop();
				break;
			}
			case '[':
			{
				brackets.push(false);
				break;
			}
			case ']':
			{
				if (brackets.empty()) return "No";
				if (brackets.top()) return "No";
				brackets.pop();
				break;
			}
			default: pass;
		}
	}

	if (!brackets.empty()) return "No";
	return "Yes";
}


int main(){
	cin >> n;
	getline(cin, plain_text);

	for (int i = 0; i < n; i++){
		getline(cin, plain_text);
		cout << check_brackets() << endl;
	}
}