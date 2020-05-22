#include <iostream>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int n, m;
	cin >> n >> m;

	int* ar = new int[n];
	if (!ar)
		return 0x1;

	for (int i = 0; i < n; ++i)
		cin >> ar[i];

	int last_s = 0;
	for (int i = 0; i < n - 2; ++i)
		for (int j = i + 1; j < n - 1; ++j)
			for (int k = j + 1; k < n; ++k)
			{
				int s = ar[i] + ar[j] + ar[k];
				if (s <= m && m - s < m - last_s)
					last_s = s;
			}

	cout << last_s << '\n';

	delete[] ar;

	return 0;
}