#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

struct Circle
{
    int idx, x, y, r;
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    cin >> n;

    vector<Circle> c(n);
    for (int i = 0; i < n; ++i)
    {
        c[i].idx = i;
        cin >> c[i].x >> c[i].y >> c[i].r;
    }

    sort(c.begin(), c.end(), [](const auto& a, const auto& b) {
        return a.r > b.r || (a.r == b.r && a.idx < b.idx);
    });

    map<int, map<int, vector<int> > > grid;
    vector<int> results(n);
    int last_r = 0;
    for (int i = 0; i < n; ++i)
    {
        if (results[c[i].idx])
            continue;

        if (2 * c[i].r <= last_r || !last_r)
        {
            last_r = c[i].r;
            grid.clear();
            for (int j = 0; j < n; ++j)
                if (!results[c[j].idx])
                    grid[c[j].x / c[i].r][c[j].y / c[i].r].emplace_back(j);
        }

        auto xl = grid.lower_bound(c[i].x / last_r - 2);
        auto xu = grid.upper_bound(c[i].x / last_r + 2);
        for (auto xit = xl; xit != xu; ++xit)
        {
            auto yl = xit->second.lower_bound(c[i].y / last_r - 2);
            auto yu = xit->second.upper_bound(c[i].y / last_r + 2);
            for (auto yit = yl; yit != yu; ++yit)
                for (auto vit = yit->second.end() - 1; vit >= yit->second.begin(); --vit)
                {
                    long long dx = c[*vit].x - c[i].x;
                    long long dy = c[*vit].y - c[i].y;
                    long long d = c[*vit].r + c[i].r;
                    if (dx * dx + dy * dy <= d * d)
                    {
                        results[c[*vit].idx] = c[i].idx + 1;
                        yit->second.erase(vit);
                    }
                }
        }
    }

    for (int i = 0; i < n; ++i)
    {
        if (i)
            cout << ' ';
        cout << results[i];
    }
    cout << '\n';

    return 0;
}
