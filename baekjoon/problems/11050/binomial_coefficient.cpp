#include <iostream>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int n, k;
	cin >> n >> k;

	int s = 1;
	for (int i = n - k + 1; i <= n; ++i)
		s *= i;
	for (int i = 2; i <= k; ++i)
		s /= i;

	cout << s << '\n';

	return 0;
}