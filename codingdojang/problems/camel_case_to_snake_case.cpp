// Problem: http://codingdojang.com/scode/484?answer_mode=hide

#include <iostream>
#include <string>

using namespace std;

int main()
{
	string s;

	s.reserve(128);
	cin >> s;

	for (auto it = s.begin(); it != s.end(); it++)
	{
		if (isupper(*it) || isdigit(*it))
		{
			*it = tolower(*it);
			if (it == s.begin())
				continue;
			s.insert(it, '_');
			it++;
		}
	}

	cout << s << endl;
	return 0;
}