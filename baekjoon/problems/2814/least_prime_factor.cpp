#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

using ull = unsigned long long;

constexpr ull MAX_PRIME = 100'000;
constexpr ull MAX_RESULT = 1'000'000'000;

void sieve(vector<ull>& p)
{
    vector<bool> b(MAX_PRIME + 1, true);
    ull n = static_cast<ull>(sqrtl(MAX_PRIME)), i, j;

    p = { 2 };

    for (i = 3; i <= n; i += 2)
        if (b[i])
        {
            p.emplace_back(i);
            for (j = i * i; j <= MAX_PRIME; j += 2 * i)
                b[j] = false;
        }

    for (; i <= MAX_PRIME; i += 2)
        if (b[i])
            p.emplace_back(i);
}

ull count_num(ull i, ull factor, ull k, ull p, const vector<ull>& primes)
{
    ull factor2 = primes[i] * factor;
    if (factor2 > k || primes[i] >= p)
        return 0;

    ull c = k / factor2;
    c += count_num(i + 1, factor, k, p, primes);
    c -= count_num(i + 1, factor2, k, p, primes);

    return c;
}

ull solve(ull n, ull p)
{
    if (n <= 1)
        return p;
    if (p * p > MAX_RESULT)
        return 0;
    if (n == 2)
        return p * p;

    vector<ull> primes;
    sieve(primes);

    ull l = p * (p + 1), u = MAX_RESULT + 1;
    while (l < u)
    {
        ull m = (l + u) / 2;
        ull c = m / p - count_num(0, p, m, p, primes);

        if (c < n)
            l = m + 1;
        else
            u = m;
    }

    return (l > MAX_RESULT) ? 0 : l;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    ull n, p;
    cin >> n >> p;
    cout << solve(n, p) << '\n';

    return 0;
}