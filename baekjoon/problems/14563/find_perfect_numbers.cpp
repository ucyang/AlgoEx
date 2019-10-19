// Problem: https://www.acmicpc.net/problem/14563

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	unsigned long long n;
	unsigned long long i, j;
	unsigned long long square_root;
	unsigned long long sum;

	cin >> n;

	while (n--)
	{
		cin >> i;

		sum = 1;
		square_root = static_cast<int>(sqrt(i));

		for (j = 2; j <= square_root; j++)
		{
			if (i % j == 0)
			{
				if (j >= i / j)
				{
					if (j == square_root)
						sum += j;
					break;
				}
				sum += j + i / j;
			}
		}

		if (sum == i && i != 1)
			cout << "Perfect" << endl;
		else if (sum < i || i == 1)
			cout << "Deficient" << endl;
		else
			cout << "Abundant" << endl;
	}

	return 0;
}
