#include <iostream>

int main()
{
	char chr;
	int cur_amount = 0, cur_min = 0, min_amount = 0;

	while (true){
		chr = getc(stdin);
		if (chr != ')' && chr != '(')
			break;

		cur_amount += chr == '(' ? 1 : -1;

		if (cur_amount < cur_min){
			min_amount = 1;
			cur_min = cur_amount;
		}
		else if (cur_amount == cur_min) min_amount++;
	}

	printf("%d\n", cur_amount == 0 ? min_amount : 0);

	return 0;
}