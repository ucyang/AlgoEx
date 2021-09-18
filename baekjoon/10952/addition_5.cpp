#include <iostream>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	while (true)
	{
		int a, b;
		cin >> a >> b;
		if (!a && !b)
			break;
		cout << a + b << '\n';
	}

	return 0;
}