// Problem: http://codingdojang.com/scode/393?answer_mode=hide

#include <iostream>

using namespace std;

int main()
{
	int count = 0;
	int i, j;

	for (i = 1; i < 10000; i++)
	{
		j = i;
		do
		{
			if (j % 10 == 8)
				count++;
		} while (j /= 10);
	}
	cout << count << endl;
	return 0;
}