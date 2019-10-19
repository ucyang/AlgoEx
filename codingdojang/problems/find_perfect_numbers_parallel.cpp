// Problem: http://codingdojang.com/scode/539?answer_mode=hide

#include <omp.h>
#include <iostream>

using namespace std;

int main()
{
	const int num_threads = 4;
	int tid;

	unsigned long long n;
	unsigned long long i, j;
	unsigned long long square_root;
	unsigned long long sum;

	omp_set_num_threads(num_threads);

	cin >> n;
	cout << endl;

#pragma omp parallel private(tid, i, j, square_root, sum)
	{
		tid = omp_get_thread_num();

		for (i = 2 + tid; i <= n; i += num_threads)
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
#pragma omp critical
				cout << i << endl;
		}
	}
	return 0;
}