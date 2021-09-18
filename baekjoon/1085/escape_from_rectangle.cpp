#include <iostream>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int x, y, w, h;
	cin >> x >> y >> w >> h;

	int mx = (x < w - x) ? x : w - x;
	int my = (y < h - y) ? y : h - y;
	cout << ((mx < my) ? mx : my) << '\n';

	return 0;
}