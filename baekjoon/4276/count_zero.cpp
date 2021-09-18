// Problem: https://www.acmicpc.net/problem/4276

#include <iostream>

using namespace std;

unsigned long long CountZeros(long long n)
{
	unsigned long long count = 1;
	unsigned long long i = 1;
	unsigned long long a, b, c;

	if (n < 0)
		return 0;

	while (true)
	{
		a = n / i / 10;
		b = n / i % 10;
		c = n % i;

		if (!a)
			break;
		if (!b)
			count += (a - 1) * i + c + 1;
		else
			count += a * i;

		i *= 10;
	}

	return count;
}

int main()
{
	long long n, m;

	while (true)
	{
		cin >> n >> m;
		if (n < 0)
			break;
		cout << CountZeros(m) - CountZeros(n - 1) << endl;
	}

	return 0;
}
