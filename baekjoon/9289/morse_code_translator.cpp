// Problem: https://www.acmicpc.net/problem/9289

#include <iostream>
#include <string>
#include <sstream>
#include <unordered_map>
#include <limits>

using namespace std;

unordered_map<string, char> m{
	{ ".-", 'A' },
	{ "-...", 'B' },
	{ "-.-.", 'C' },
	{ "-..", 'D' },
	{ ".", 'E' },
	{ "..-.", 'F' },
	{ "--.", 'G' },
	{ "....", 'H' },
	{ "..", 'I' },
	{ ".---", 'J' },
	{ "-.-", 'K' },
	{ ".-..", 'L' },
	{ "--", 'M' },
	{ "-.", 'N' },
	{ "---", 'O' },
	{ ".--.", 'P' },
	{ "--.-", 'Q' },
	{ ".-.", 'R' },
	{ "...", 'S' },
	{ "-", 'T' },
	{ "..-", 'U' },
	{ "...-", 'V' },
	{ ".--", 'W' },
	{ "-..-", 'X' },
	{ "-.--", 'Y' },
	{ "--..", 'Z' },
};

int main()
{
	int n;
	string morse_code;
	stringstream ss;

	cin >> n;
	cin.ignore(numeric_limits<streamsize>::max(), '\n');

	for (int i = 1; i <= n; i++)
	{
		getline(cin, morse_code);
		ss.clear();
		ss.str(morse_code);
		cout << "Case " << i << ": ";
		while (getline(ss, morse_code, ' '))
			cout << m[morse_code];
		cout << endl;
	}

	return 0;
}
