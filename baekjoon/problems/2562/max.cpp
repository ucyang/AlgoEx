#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int ar[9];
	for (int i = 0; i < 9; ++i)
		cin >> ar[i];

	auto it = max_element(ar, ar + 9);
	cout << *it << '\n'
		<< it - ar + 1 << '\n';

	return 0;
}