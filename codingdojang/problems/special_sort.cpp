// Problem: http://codingdojang.com/scode/414?answer_mode=hide

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int ar[] = { -1, 1, 3, -2, 2 };

	stable_sort(&ar[0], &ar[sizeof(ar) / sizeof(ar[0])],
		[](auto a, auto b) { return (a < 0) && (b >= 0); });
	
	for (auto i : ar)
		cout << i << " ";
	cout << endl;
	return 0;
}