#include <iostream>

using namespace std;

int main()
{
    unsigned long long n, p;
    unsigned long long s = 1;

    cin >> n >> p;

    while (n > 1)
        s = s * n-- % p;

    cout << s << '\n';

    return 0;
}
