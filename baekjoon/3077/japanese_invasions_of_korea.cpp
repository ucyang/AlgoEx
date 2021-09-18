#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

int main()
{
    int n, i, j;
    string s;
    unordered_map<string, int> m;
    vector<int> v;
    int score = 0;

    cin.sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n;

    v.reserve(n);

    for (i = 0; i < n; ++i)
    {
        cin >> s;
        m[s] = i;
    }

    for (i = 0; i < n; ++i)
    {
        cin >> s;
        v.emplace_back(m[s]);
    }

    for (i = 0; i < n - 1; ++i)
        for (j = i + 1; j < n; ++j)
            if (v[i] < v[j])
                ++score;

    cout << score << '/' << n * (n - 1) / 2 << '\n';

    return 0;
}
