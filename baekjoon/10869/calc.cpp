#include <iostream>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int a, b;
	cin >> a >> b;

	cout << a + b << '\n'
		<< a - b << '\n'
		<< a * b << '\n'
		<< a / b << '\n'
		<< a % b << '\n';

	return 0;
}