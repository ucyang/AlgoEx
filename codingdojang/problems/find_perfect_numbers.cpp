// Problem: http://codingdojang.com/scode/539?answer_mode=hide

#include <iostream>

using namespace std;

int main()
{
	unsigned long long n;
	unsigned long long i, j;
	unsigned long long square_root;
	unsigned long long sum;

	cin >> n;
	cout << endl;

	for (i = 2; i <= n; i++)
	{
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

		if (i == sum)
			cout << i << endl;
	}
	return 0;
}