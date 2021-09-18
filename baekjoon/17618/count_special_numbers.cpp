#include <iostream>

using namespace std;

int main()
{
    int n, i, sum, count = 0;

    cin >> n;

    for (; n; --n)
    {
        for (i = n, sum = 0; i; i /= 10)
            sum += i % 10;
        if (n % sum == 0)
            ++count;
    }

    cout << count << endl;

    return 0;
}
