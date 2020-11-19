#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define MAX_POWER 10

void get_coeffs(int* coefficients){
	vector<string> params;
	int keywords = 1;
	string begin;

	cin >> begin;
	params.push_back("1");

	while (true){
		string keyword;
		cin >> keyword;

		if (keyword == "END"){
			keywords--;
			params.pop_back();
			if (keywords == 0)
				break;
		}
		else if (keyword == "LOOP"){
			keywords++;

			string param;
			cin >> param;

			params.push_back(param);
		}
		else if (keyword == "OP"){
			string num;
			cin >> num;

			int coefficient = stoi(num);
			int multiplier = 1;
			int pow = 0;

			for (string param : params){
				if (param == "n") pow++;
				else multiplier *= stoi(param);
			}

			coefficients[pow] += coefficient * multiplier;
		}
	}
}

string to_string(int* coefficients){
	string result;

	for (int i = MAX_POWER; i > 0; i--){
		if (coefficients[i] != 0){
			if (coefficients[i] == 1) result += "n";
			else if (coefficients[i] == -1) result += "-n";
			else{
				result += to_string(coefficients[i]);
				result += "*n";
			}

			if (i != 1){
				result += "^";
				result += to_string(i);
			}
		}

		if (coefficients[i - 1] > 0 && result.length() != 0) result += "+";
	}

	if (result.length() == 0 || coefficients[0] != 0) result += to_string(coefficients[0]);

	return result;
}

int main(){
	int n;
	cin >> n;

	int coefficients[MAX_POWER + 1];

	for (int i = 1; i <= n; i++){
		cout << "Program #" << i << endl;

		fill(coefficients, coefficients + MAX_POWER + 1, 0);
		get_coeffs(coefficients);

		cout << "Runtime = " << to_string(coefficients) << endl;

		if (i != n) cout << endl;
	}

	return 0;
}