// Problem: http://codingdojang.com/scode/428?answer_mode=hide

#include <iostream>
#include <string>
#include <iterator>
#include <algorithm>

using namespace std;

int main()
{
	string str, str2;

	cin >> str;
	transform(str.cbegin(), str.cend(), back_inserter(str2), [](auto c) {
		static bool even = true;

		even = !even;
		if (even)
			if (isdigit(c))
				return '*';
		return c;
	});
	cout << str2 << endl;
	return 0;
}