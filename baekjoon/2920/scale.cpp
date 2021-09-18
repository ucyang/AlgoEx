#include <iostream>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	bool asc = true, desc = true;
	int a, b;

	cin >> a;
	for (int i = 1; i < 8; ++i)
	{
		cin >> b;
		if (a < b)
			desc = false;
		else if (a > b)
			asc = false;
		a = b;
	}

	if (asc)
		cout << "ascending\n";
	else if (desc)
		cout << "descending\n";
	else
		cout << "mixed\n";

	return 0;
}