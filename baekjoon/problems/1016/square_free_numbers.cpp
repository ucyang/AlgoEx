#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	size_t m, M;
	cin >> m >> M;
    
    vector<bool> b(M - m + 1);
    size_t n = static_cast<size_t>(sqrtl(static_cast<long double>(M)));
    for (size_t i = 2; i <= n; ++i)
    {
        size_t a = i * i, q = m / a + 1;
        if (m % a == 0)
            b[0] = true;
        for (size_t t = a * q; t <= M; t = a * ++q)
            b[t - m] = true;
    }

    cout << count(b.cbegin(), b.cend(), false) << '\n';

	return 0;
}