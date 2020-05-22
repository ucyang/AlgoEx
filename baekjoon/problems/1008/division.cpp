#include <iostream>

using namespace std;

int main()
{
	int a, b;
	cin >> a >> b;
	cout.precision(10);
	cout << static_cast<double>(a) / b << '\n';
	return 0;
}