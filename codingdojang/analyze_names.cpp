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

	wcout << L"김씨: "
		<< count_if(v.cbegin(), v.cend(), [](auto s) { return s[0] == L'김'; })
		<< L"명\n";
	wcout << L"이씨: "
		<< count_if(v.cbegin(), v.cend(), [](auto s) { return s[0] == L'이'; })
		<< L"명\n\n";

	wcout << L"이재영: " << count(v.cbegin(), v.cend(), L"이재영") << L"명\n\n";

	sort(v.begin(), v.end());
	v.erase(unique(v.begin(), v.end()), v.cend());
	wcout << L"총 " << v.size() << L"명(중복 제외)\n\n";

	wcout << L"오름차순(중복 제외):\n";
	for (auto s : v)
		wcout << s << endl;

	wcin.ignore();
	return 0;
}