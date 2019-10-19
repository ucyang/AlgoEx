// Problem: http://codingdojang.com/scode/469?answer_mode=hide

#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

map<string, char> m{
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
	string morse_code;
	size_t pos;
	stringstream ss;
	vector<string> words;

	getline(cin, morse_code);

	while ((pos = morse_code.find("  ")) != string::npos)
	{
		words.emplace_back(morse_code.substr(0, pos));
		morse_code.erase(0, pos + 2);
	}
	words.emplace_back(morse_code.substr(0, pos));

	for (auto word : words)
	{
		ss.clear();
		ss.str(word);
		while (getline(ss, morse_code, ' '))
		{
			cout << m[morse_code];
		}
		cout << ' ';
	}

	cout << endl;
	return 0;
}