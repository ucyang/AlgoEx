#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

using ull = unsigned long long;

constexpr ull MAX_PRIME = 1'000'000;

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

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    ull m, n;
    cin >> m >> n;

    vector<ull> p;
    sieve(p);

    auto l = lower_bound(p.cbegin(), p.cend(), m);
    auto u = upper_bound(p.cbegin(), p.cend(), n);
    for (auto it = l; it != u; ++it)
        cout << *it << '\n';

    return 0;
}