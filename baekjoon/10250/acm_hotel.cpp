#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int t;
	cin >> t;

	cout.fill('0');
	while (t--)
	{
		int h, w, n;
		cin >> h >> w >> n;
		cout << setw(1) << (n - 1) % h + 1
			<< setw(2) << (n - 1) / h + 1 << '\n';
	}

	return 0;
}