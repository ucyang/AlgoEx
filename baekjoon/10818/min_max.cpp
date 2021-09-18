#include <iostream>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int n;
	cin >> n;

	int min_i, max_i;
	cin >> min_i;
	max_i = min_i;

	while (--n)
	{
		int i;
		cin >> i;
		if (i < min_i)
			min_i = i;
		else if (i > max_i)
			max_i = i;
	}

	cout << min_i << ' ' << max_i << '\n';

	return 0;
}