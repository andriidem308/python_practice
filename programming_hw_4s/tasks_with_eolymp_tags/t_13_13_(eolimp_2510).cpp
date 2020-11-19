#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;

int main()
{
	unsigned n, k;
	int *numbers, *order;
	queue<int> *queues;

	scanf("%u", &n);

	numbers = new int[n];
	for(int i = 0; i < n; i++) scanf("%d", numbers + i);

	scanf("%u", &k);
	queues = new queue<int>[k];

	order = new int[n];

	for(int i = 0; i < n; i++){
		int fit = find_if(queues, queues + k,
		                  [&](const queue<int> &q){return q.empty() || q.back() <= numbers[i];}) - queues;

		if(fit >= k) {
			puts("NO");
			return 0;
		}

		queues[fit].push(numbers[i]);
		order[i] = fit + 1;
	}

	puts("YES");

	for(int i = 0; i < n; i++) printf("I(%d)\n", order[i]);

	for(int i = 0; i < n; i++){
		queue<int>* min_elem = min_element(queues, queues + k,
		                                   [&](const queue<int> x, const queue<int> y){
			                                  return !x.empty() && !y.empty() && x.front() < y.front();
		                                  });
		min_elem->pop();
		printf("R(%d)\n", min_elem - queues + 1);
	}

	return 0;
}