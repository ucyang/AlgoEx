#include <iostream>
#include <numeric>
#include <algorithm>
#include <map>
#include <cmath>
#include <ctime>

using namespace std;

unsigned long long power_mod(unsigned long long x, unsigned long long y,
        unsigned long long p)
{
    unsigned long long result = 1;

    x %= p;
    y %= p;

    while (y > 0)
    {
        if (y & 1)
            result = static_cast<unsigned __int128>(result) * x % p;
        y >>= 1;
        x = static_cast<unsigned __int128>(x) * x % p;
    }

    return result;
}

bool is_prime(unsigned long long n)
{
    static constexpr unsigned long long a[] = {
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37
    };
    static constexpr size_t an = sizeof(a) / sizeof(a[0]);
    unsigned long long d = n - 1;
    unsigned long long d_save = d;
    unsigned long long x;
    bool flag;

    if (n < 41)
        return find(a, a + an, n) != a + an;

    while (d % 2 == 0)
        d /= 2;

    for (size_t i = 0; i < an; ++i)
    {
        x = power_mod(a[i], d, n);
        if (x == 1 || x == n - 1)
           continue;

        flag = false;
        while (d != n - 1)
        {
            x = static_cast<unsigned __int128>(x) * x % n;
            d *= 2;

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

__int128 mods(__int128 a, __int128 n)
{
    a %= n;
    if ((a > 0 && n < 0) || (a < 0 && n > 0))
        a += n;
    return (2 * a > n) ? a - n : a;
}

long long power_mods(long long x, unsigned long long y, unsigned long long p)
{
    long long result = 1;

    x %= p;
    y %= p;

    while (y > 0)
    {
        if (y & 1)
            result = mods(static_cast<__int128>(result) * x, p);
        y >>= 1;
        x = mods(static_cast<__int128>(x) * x, p);
    }

    return result;
}

long long quos(__int128 a, __int128 n)
{
    return (a - mods(a, n)) / n;
}

pair<unsigned long long, unsigned long long> sq2(unsigned long long p)
{
    long long a;
    unsigned long long k = (p - 1) / 4;
    unsigned long long i = 2;
    __int128 n;
    long long w0, w1, z0, z1, u0, u1;
    long long t, t2;

    do
    {
        a = power_mods(i, k, p);
        t = mods(static_cast<__int128>(a) * a, p);
        ++i;
    } while (t != -1);

    for (w0 = p, w1 = 0, z0 = a, z1 = 1; z0 != 0 || z1 != 0;)
    {
        n = static_cast<__int128>(z0) * z0 + static_cast<__int128>(z1) * z1;

        u0 = quos(static_cast<__int128>(w0) * z0
                + static_cast<__int128>(w1) * z1, n);
        u1 = quos(static_cast<__int128>(w1) * z0
                - static_cast<__int128>(w0) * z1, n);

        t = w0;
        t2 = z0;
        w0 = z0;
        z0 = t - static_cast<__int128>(z0) * u0
            + static_cast<__int128>(z1) * u1;

        t = w1;
        w1 = z1;
        z1 = t - static_cast<__int128>(t2) * u1
            - static_cast<__int128>(z1) * u0;
    }

    return make_pair(abs(w0), abs(w1));
}

unsigned long long pollard_rho(unsigned long long n)
{
    unsigned long long x, y, c, d, i, k;

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
            d = __gcd(static_cast<unsigned long long>(
                        abs(static_cast<long long>(x - y))), n);

            if (i == k)
            {
                y = x;
                k <<= 1;
            }
        }
    } while (d == n);

    return d;
}

bool get_prime_factors(unsigned long long n,
        map<unsigned long long, unsigned>& prime_factors)
{
    unsigned long long factor;

    if (n < 2)
        return false;

    prime_factors.clear();
    while (true)
    {
        if (n == 1 || is_prime(n))
        {
            ++prime_factors[n];
            break;
        }

        factor = n;
        do
        {
            factor = pollard_rho(factor);
        } while (!is_prime(factor));

        do
        {
            ++prime_factors[factor];
            n /= factor;
        } while (n % factor == 0);
    }

    return true;
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

pair<unsigned long long, unsigned long long> get2_helper(unsigned long long n)
{
    unsigned long long s0, s1, m, i, j;

    s0 = sqrtl(n);
    s1 = 0;
    i = s0 * s0;
    j = s1 * s1;
    do
    {
        m = i + j;
        if (n == m)
            break;
        if (m > n)
        {
            --s0;
            i = s0 * s0;
        }
        else
        {
            ++s1;
            j = s1 * s1;
        }
    } while (s0 >= s1);

    return make_pair(s0, s1);
}

pair<unsigned long long, unsigned long long> get2(unsigned long long n)
{
    unsigned long long n1, n2;
    map<unsigned long long, unsigned> prime_factors;
    size_t np;
    auto getp = [](auto m) {
        return (m % 4 == 1 && is_prime(m)) ? sq2(m) : get2_helper(m);
    };

    get_prime_factors(n, prime_factors);
    np = prime_factors.size();
    auto it_beg = prime_factors.cbegin();

    if (np <= 1)
        n1 = pow(static_cast<long double>(it_beg->first), it_beg->second >> 1);
    else
    {
        auto it_mid = it_beg;
        auto op = [](auto i, auto p) {
            return i * pow(static_cast<long double>(p.first), p.second);
        };

        advance(it_mid, np / 2 + np % 2);
        n1 = accumulate(it_beg, it_mid, 1ULL, op);
    }
    n2 = n / n1;

    auto p1 = getp(n1);
    auto p2 = getp(n2);

    return make_pair(p1.first * p2.first + p1.second * p2.second,
            abs(static_cast<long long>(
                    p1.first * p2.second - p1.second * p2.first)));
}

int main()
{
    unsigned long long n;
    unsigned long long n_div = 1;
    unsigned long long s[4];
    unsigned long long sn = 2;
    unsigned long long i;
    map<unsigned long long, unsigned> prime_factors;
    auto get_n_div = [&]() {
        get_prime_factors(n, prime_factors);
        auto t = accumulate(prime_factors.cbegin(), prime_factors.cend(), 1ULL,
                [](auto i, auto p) {
                    return i * pow(static_cast<long double>(p.first),
                            p.second >> 1);
                });
        n /= t * t;
        n_div *= t;
    };

    srand(time(nullptr));

    cin.sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n;
    if (n < 0)
        return 0x1;

    s[0] = sqrtl(n);
    if (n == s[0] * s[0])
    {
        cout << 1 << '\n' << s[0] << '\n';
        return 0;
    }

    get_n_div();

    if (!express3(n))
    {
        for (s[3] = sqrtl(n); !express3(n - s[3] * s[3]); --s[3]);
        n -= s[3] * s[3];
        sn = 4;
        s[3] *= n_div;
        get_n_div();
    }

    if (sn > 2 || !express2(n))
    {
        for (s[2] = sqrtl(n); !express2(n - s[2] * s[2]); --s[2]);
        n -= s[2] * s[2];
        if (sn < 3)
            sn = 3;
        s[2] *= n_div;
        get_n_div();
    }

    auto p = get2(n);
    s[1] = p.first * n_div;
    s[0] = p.second * n_div;

    cout << sn << '\n';
    for (i = 0; i < sn; ++i)
    {
        if (i)
            cout << ' ';
        cout << s[i];
    }
    cout << '\n';

    return 0;
}
