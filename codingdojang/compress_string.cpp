// Problem: http://codingdojang.com/scode/465?answer_mode=hide

#include <iostream>
#include <string>

using namespace std;

int main()
{
	string raw_str;
	string compressed_str;
	string::const_iterator it, it2;

	cin >> raw_str;

	for (it = raw_str.cbegin(); it != raw_str.cend();)
	{
		it2 = it;
		while ((++it != raw_str.cend()) && (*it == *it2));
		compressed_str += *it2;
		compressed_str += to_string(it - it2);
	}

	cout << compressed_str << endl;
	return 0;
}