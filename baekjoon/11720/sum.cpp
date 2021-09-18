#include <iostream>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int n;
	cin >> n;

	int s = 0;
	while (n--)
	{
		char c;
		cin >> c;
		s += c - '0';
	}

	cout << s << '\n';

	return 0;
}