#include <iostream>
#include <string>

using namespace std;

struct Student
{
	string Name, Surname;
	short int Class;
	char Letter;
	int Day, Month, Year;
};


bool operator>(const Student &a, const Student &b){
	if (a.Class > b.Class) return true;

	if (a.Class == b.Class) {
		if (a.Letter > b.Letter) return true;

		if (a.Letter == b.Letter) {
			if (a.Surname > b.Surname) return true;

			if (a.Surname == b.Surname) {
				if (a.Name > b.Name) return true;
			}
		}
	}

	return false;
};

void swap(Student &st_1, Student &st_2)
{
	Student tmp = st_1;
	st_1 = st_2;
	st_2 = tmp;
};

void scan_date(int &day, int &month, int &year)
{
	string temp;
	cin >> temp;

	day = atoi(temp.substr(0, 2).c_str());
	month = atoi(temp.substr(3, 2).c_str());
	year = atoi(temp.substr(6, 2).c_str());
}

void nine_zero(int k)
{
	if (k > 9) cout << k;
	else cout << "0" << k;
}

void date_output(int dd,int  mm,int  yy){
	nine_zero(dd);
	cout << ".";
	nine_zero(mm);
	cout << ".";
	nine_zero(yy);
	cout << endl;
}


int main()
{
	int n;
	cin >> n;

	Student *a = new Student[n];
	for (int i = 0; i < n; i++)
	{
		cin >> a[i].Surname >> a[i].Name >> a[i].Class >> a[i].Letter;
		scan_date(a[i].Day, a[i].Month, a[i].Year);
	}

	for (int k = 2; k <= n; k++)
	{
		for (int i = 0; i <= n - k; i++)
			if (a[i] > a[i + 1])
				swap(a[i], a[i + 1]);;
	}

	for (int i = 0; i < n; i++)
	{
		cout << a[i].Class << a[i].Letter << " " << a[i].Surname << " " << a[i].Name << " ";
		date_output(a[i].Day, a[i].Month, a[i].Year);
	}


	return 0;
}
