// Problem: http://codingdojang.com/scode/488?answer_mode=hide

#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int main()
{
	string str;

	getline(cin, str);

	stringstream ss(str);

	while (getline(ss, str, ' '))
	{
		sort(str.begin(), str.end());

		if (str == "0123456789")
			cout << "true ";
		else
			cout << "false ";
	}

	cout << endl;
	return 0;
}