#include <iostream>
#include <string>

using namespace std;

void order_split(const string& direct, const string& center) {
	string root, left_center, right_center, left_direct, right_direct;
	size_t root_center_position, left_center_size;

	root = direct.substr(0, 1);
	root_center_position = center.find(root);

	left_center = center.substr(0, root_center_position);
	right_center = center.substr(root_center_position + 1);

	left_center_size = left_center.size();

	left_direct = direct.substr(1, left_center_size);
	right_direct = direct.substr(left_center_size + 1);

	if(!left_direct.empty() && !left_center.empty())
		order_split(left_direct, left_center);
	if(!right_direct.empty() && !right_center.empty())
		order_split(right_direct, right_center);

	cout << root;
}

void split_procedure(const string & direct, const string & center) {
	order_split(direct, center); cout << "\n";
}

int main() {
	unsigned int number;
	cin >> number;

	for (unsigned int i = 0; i < number; i++) {
		unsigned int len;
		string direct, center;

		cin >> len;
		cin >> direct >> center;

		split_procedure(direct, center);
	}

	return 0;
}
