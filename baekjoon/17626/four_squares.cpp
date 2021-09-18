#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

using ll = long long;
using ull = unsigned long long;

ull power_mod(ull x, ull y, ull p)
{
    ull ret = 1;

    for (x %= p, y %= p; y > 0; y >>= 1)
    {
        if (y & 1)
            ret = static_cast<unsigned __int128>(ret) * x % p;
        x = static_cast<unsigned __int128>(x) * x % p;
    }

    return ret;
}

bool is_prime(ull n)
{
    static constexpr ull a[] = {
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37
    };
    static constexpr size_t an = sizeof(a) / sizeof(a[0]);
    ull d = n - 1, d_save = d, x;
    bool flag;

    if (n < 41)
        return binary_search(a, a + an, n);

    while (d % 2 == 0)
        d >>= 1;

    for (size_t i = 0; i < an; ++i)
    {
        x = power_mod(a[i], d, n);
        if (x == 1 || x == n - 1)
            continue;

        flag = false;
        while (d != n - 1)
        {
            x = static_cast<unsigned __int128>(x) * x % n;
            d <<= 1;

            if (x == 1)
                return false;
            if (x == n - 1)
            {
                flag = true;
                break;
            }
        }
        if (!flag)
            return false;
        d = d_save;
    }

    return true;
}

ull pollard_rho(ull n)
{
    ull x, y, c, d, i, k;

    if (n == 1)
        return 1;
    if (n % 2 == 0)
        return 2;

    do
    {
        x = y = rand() % (n - 2) + 2;
        c = rand() % (n - 1) + 1;

        for (i = 1, k = 2, d = 1; d == 1; ++i)
        {
            x = (power_mod(x, 2, n) + c) % n;
            d = __gcd(static_cast<ull>(abs(static_cast<ll>(x - y))), n);

            if (i == k)
            {
                y = x;
                k <<= 1;
            }
        }
    } while (d == n);

    return d;
}

bool express3(unsigned long long n)
{
    unsigned long long i;
    for (i = n; i % 8 != 7 && i % 4 == 0; i /= 4);
    return i % 8 != 7;
}

bool express2(unsigned long long n)
{
    unsigned long long factor;
    unsigned i;

    while (n > 2)
    {
        if (is_prime(n))
            return n % 4 == 1;

        factor = n;
        do
        {
            factor = pollard_rho(factor);
        } while (!is_prime(factor));

        i = 0;
        do
        {
            ++i;
            n /= factor;
        } while (n % factor == 0);

        if (factor % 4 == 3 && i % 2)
            return false;
    }

    return true;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    ull n;
    cin >> n;

    ull i = sqrtl(n);
    if (i * i == n)
        cout << 1;
    else if (express2(n))
        cout << 2;
    else if (express3(n))
        cout << 3;
    else
        cout << 4;
    cout << '\n';

    return 0;
}