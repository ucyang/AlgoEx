// Problem: http://codingdojang.com/scode/410?answer_mode=hide

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

int main()
{
	wcin.imbue(locale("korean"));
	wcout.imbue(locale("korean"));

	wstring str;

	wcin >> str;
	wcout << endl;

	wstringstream ss(str);
	vector<decltype(str)> v;

	while (getline(ss, str, L','))
		v.emplace_back(str);

	wcout << L"�达: "
		<< count_if(v.cbegin(), v.cend(), [](auto s) { return s[0] == L'��'; })
		<< L"��\n";
	wcout << L"�̾�: "
		<< count_if(v.cbegin(), v.cend(), [](auto s) { return s[0] == L'��'; })
		<< L"��\n\n";

	wcout << L"���翵: " << count(v.cbegin(), v.cend(), L"���翵") << L"��\n\n";

	sort(v.begin(), v.end());
	v.erase(unique(v.begin(), v.end()), v.cend());
	wcout << L"�� " << v.size() << L"��(�ߺ� ����)\n\n";

	wcout << L"��������(�ߺ� ����):\n";
	for (auto s : v)
		wcout << s << endl;

	wcin.ignore();
	return 0;
}