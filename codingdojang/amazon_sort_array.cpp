// Problem: http://codingdojang.com/scode/416?answer_mode=hide

#include <iostream>
#include <vector>

using namespace std;

int main()
{
	vector<int> v = {
		11, 12, 13, 14, 15,
		21, 22, 23, 24, 25,
	};
	const int N = v.size();
	auto sit = v.cbegin();
	
	if (N <= 2)
		return 1;

	for (int i = 1, j = N / 2, tmp; j < N - 1; i += 2, j++)
	{
		tmp = v[j];
		v.erase(sit + j);
		v.emplace(sit + i, tmp);
	}

	for (auto i : v)
		cout << i << " ";
	cout << endl;
	return 0;
}