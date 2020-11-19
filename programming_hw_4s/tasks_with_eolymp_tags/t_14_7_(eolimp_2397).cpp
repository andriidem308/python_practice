#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main(){
	int n;
	int x, y, h, w;
	int counter = 0, result = 0;
	set <int> cur_set;

	cin >> n;
	vector <vector<int>> state(2005, vector <int> (2005));

	while(n--){
        counter++;

        scanf("%d %d %d %d", &x, &y, &w, &h);

        for (int i = x; i < x + w; i++) {
	        for (int j = y; j < y + h; j++) {
	        	state[i][j] = counter;
	        }
        }
    }

    for (int i = 0; i < 2005; i++) {
	    for (int j = 0; j < 2005; j++) {
		    if (cur_set.count(state[i][j]) == 0) {
			    result++;
			    cur_set.insert(state[i][j]);
		    }
	    }
    }

    cout << result - 1 << endl;
}
