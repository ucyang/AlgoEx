// Problem: http://codeup.kr/JudgeOnline/problem.php?id=1430

#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main()
{
	set<int> s;
	vector<bool> v;
	int n;
	int i;

	cin >> n;
	while (n--)
	{
		cin >> i;
		s.emplace(i);
	}

	cin >> n;
	while (n--)
	{
		cin >> i;
		v.emplace_back(s.find(i) != s.cend());
	}

	for (bool b : v)
		cout << b << " ";
	return 0;
}