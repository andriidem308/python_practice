#include <stdio.h>
#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int main(){
	int n;
	int number;
	stringstream my_stream;

	while (cin >> n, getchar(), n != 0){
		string s;
		getline(cin, s, '\n');

		while (s != "0"){
			vector<int> dock;

			my_stream.str("");
			my_stream.clear();
			my_stream << s;
			my_stream >> number;

			for (int i = 1; i <= n; i++){
				dock.push_back(i);

				while (!dock.empty() && number == dock.back()){
					dock.pop_back();
					my_stream >> number;
				}
			}

			cout << (dock.empty() ? "Yes" : "No") << endl;
			getline(cin, s, '\n');
		}

		cout << endl;
	}
}