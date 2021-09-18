#include <iostream>
#include <string>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int t;
	cin >> t;

	while (t--)
	{
		int r;
		cin >> r;
		string s;
		cin >> s;
		for (auto c : s)
			for (int i = 0; i < r; ++i)
				cout << c;
		cout << '\n';
	}

	return 0;
}