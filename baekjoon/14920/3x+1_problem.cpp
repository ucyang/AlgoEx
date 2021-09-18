// Problem: https://www.acmicpc.net/problem/14920

#include <iostream>

using namespace std;

int main()
{
	unsigned long long i;
	unsigned long long cycle = 1;

	cin >> i;

	while (i > 1)
	{
		if (i % 2)
			i = 3 * i + 1;
		else
			i /= 2;

		cycle++;
	}

	cout << cycle << endl;

	return 0;
}
