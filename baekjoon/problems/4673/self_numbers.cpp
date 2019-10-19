// Problem: https://www.acmicpc.net/problem/4673

#include <iostream>
#include <unordered_map>

using namespace std;

int main()
{
	const int N = 10000;
	unordered_map<int, int> m;
	int sum;
	int i, j;

	for (i = 1; i < N; i++)
	{
		sum = j = i;
		do
		{
			sum += j % 10;
		} while (j /= 10);
		m[sum] = i;
	}

	for (i = 1; i < N; i++)
		if (m.find(i) == m.cend())
			cout << i << endl;

	return 0;
}
