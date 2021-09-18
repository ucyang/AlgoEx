//Probleam: http://codingdojang.com/scode/431?answer_mode=hide

#include <iostream>

using namespace std;

int main()
{
	long long n;
	long long i;
	int c;

	while (1)
	{
		cin >> n;
		if ((n == 0) || ((n % 2) == 0) || ((n % 5) == 0))
			return 1;

		for (i = 1; i > 0; i = 10 * i + 1)
		{
			if ((i % n) == 0)
			{
				c = 1;
				while (i /= 10)
					c++;
				cout << c << endl;
				break;
			}
		}
		if (i < 0)
			return 2;
	}
	return 0;
}