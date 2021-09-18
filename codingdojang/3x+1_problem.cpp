// Problem: http://codingdojang.com/scode/409?answer_mode=hide

#include <iostream>

using namespace std;

int main()
{
	unsigned long long i, j, k, n;
	unsigned long long cycle, max_cycle = 1;

	cin >> i >> j;
	cout << endl;

	for (k = i; k <= j; k++)
	{
		n = k;
		cycle = 1;

		while (n > 1)
		{
			if (n % 2)
				n = 3 * n + 1;
			else
				n /= 2;

			cycle++;
		}

		if (cycle > max_cycle)
			max_cycle = cycle;
	}

	cout << i << " " << j << " " << max_cycle << endl;
	return 0;
}