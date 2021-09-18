// Problem: http://codingdojang.com/scode/505?answer_mode=hide

#include <iostream>

using namespace std;

int main()
{
	int sum = 0;
	int mul;
	int i, j;

	for (i = 10; i <= 1000; i++)
	{
		j = i;
		mul = 1;

		do
		{
			mul *= j % 10;
		} while (j /= 10);

		sum += mul;
	}

	cout << sum << endl;
	return 0;
}