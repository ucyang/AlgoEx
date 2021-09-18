// Problem: http://codingdojang.com/scode/408?answer_mode=hide

#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <numeric>

using namespace std;

int main()
{
	vector<int> v{ 1, 3, 4, 8, 13, 17, 20 }; // modifiable input data
	vector<int> diff;
	int diff_size;
	int min_diff;

	sort(v.begin(), v.end());
	adjacent_difference(v.cbegin(), v.cend(), back_inserter(diff));
	diff_size = diff.size();
	min_diff = *min_element(diff.cbegin() + 1, diff.cend());

	for (int i = 1; i < diff_size; i++)
	{
		if (diff[i] == min_diff)
			cout << "(" << v[i - 1] << ", " << v[i] << ")" << endl;
	}
	return 0;
}