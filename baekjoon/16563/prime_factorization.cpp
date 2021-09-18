// Reference: https://sbrus1213.tistory.com/5

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

using ull = unsigned long long;

constexpr ull MAX_PRIME = 5'000'000;

void get_min_factors(vector<ull>& min_factors)
{
    ull n = static_cast<ull>(sqrtl(MAX_PRIME));
    min_factors.assign(MAX_PRIME + 1, 0);

    for (ull i = 2; i <= n; ++i)
        if (!min_factors[i])
            for (ull j = i * i; j <= MAX_PRIME; j += i)
                if (!min_factors[j])
                    min_factors[j] = i;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    ull n;
    cin >> n;

    vector<ull> min_factors;
    get_min_factors(min_factors);

    while (n--)
    {
        ull k;
        cin >> k;

        while (min_factors[k])
        {
            cout << min_factors[k] << ' ';
            k /= min_factors[k];
        }
        cout << k << '\n';
    }

    return 0;
}