#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

using ull = unsigned long long;

constexpr ull MAX_PRIME = 100'000;
constexpr ull MAX_RESULT = 2'000'000'000;

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

ull count_non_square_free(ull i, ull factor, ull k, const vector<ull>& p)
{
    ull factor2 = p[i] * p[i] * factor;
    if (factor2 > k)
        return 0;

    ull c = k / factor2;
    c += count_non_square_free(i + 1, factor, k, p);
    c -= count_non_square_free(i + 1, factor2, k, p);

    return c;
}

ull nth_square_free(ull n)
{
    vector<ull> p;
    sieve(p);

    ull l = 1, u = MAX_RESULT;
    while (l < u)
    {
        ull m = (l + u) / 2;
        ull c = m - count_non_square_free(0, 1, m, p);

        if (c < n)
            l = m + 1;
        else
            u = m;
    }

    return l;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    ull n;
    cin >> n;
    cout << nth_square_free(n) << '\n';

    return 0;
}