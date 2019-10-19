// Problem: http://codingdojang.com/scode/405?answer_mode=hide

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream f_in;
	ofstream f_out;

	string tab_space;
	int tab_space_len;

	string str;
	string::const_iterator it;

	str.reserve(512);

	cout << "Input file name: ";
	cin >> str;
	f_in.open(str);

	if (!f_in.is_open())
	{
		cout << "Can't open input file!" << endl;
		return 1;
	}

	cout << "Output file name: ";
	cin >> str;
	f_out.open(str);

	if (!f_out.is_open())
	{
		f_in.close();
		cout << "Can't open output file!" << endl;
		return 2;
	}

	cout << "Tab space: ";
	cin.ignore();
	cin >> tab_space_len;
	tab_space.assign(tab_space_len, ' ');

	while (getline(f_in, str))
	{
		for (it = str.cbegin(); it != str.cend();)
		{
			if (*it != '\t')
				break;
			str.replace(it, it + 1, tab_space);
			it += tab_space_len;
		}
		f_out << str << endl;
	}

	f_in.close();
	f_out.close();
	return 0;
}