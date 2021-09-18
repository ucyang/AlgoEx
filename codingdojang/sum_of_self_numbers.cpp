// Problem: http://codingdojang.com/scode/365?answer_mode=hide

#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int main()
{
	map<int, int> m;
	int sum;
	int i, j;

	for (i = 1; i < 5000; i++)
	{
		sum = j = i;
		do
		{
			sum += j % 10;
		} while (j /= 10);
		m[sum] = i;
	}

	sum = 0;
	ofstream o("self_numbers_list.txt");
	bool is_open = o.is_open();

	for (i = 1; i < 5000; i++)
	{
		if (m.find(i) == m.cend())
		{
			sum += i;
			if (is_open)
				o << i << endl;
		}
	}
	if (is_open)
		o.close();
	cout << sum << endl;
	return 0;
}