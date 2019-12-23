#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

struct Point
{
    int x, y;
};

int main()
{
    Point* p;
    int dx, dy;
    int dist;
    int min_dist = INT_MAX;
    int n;
    int i, j, k;

    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n;
    p = new Point[n];

    for (i = 0; i < n; ++i)
        cin >> p[i].x >> p[i].y;

    sort(p, p + n, [](auto a, auto b) {
        return a.x < b.x || (a.x == b.x && a.y < b.y);
    });

    for (i = 0; i < n; ++i)
        for (j = i + 1; j < n; ++j)
        {
            dx = p[i].x - p[j].x;
            dy = p[i].y - p[j].y;
            if (dx * dx >= min_dist)
                break;
            if (dy * dy >= min_dist)
            {
                if (dy < 0)
                    for (k = j + 1; k < n && p[j].x == p[k].x; ++k);
                else
                    for (k = j + 1; k < n && p[j].x == p[k].x; ++k)
                    {
                        dy = p[i].y - p[k].y;
                        if (dy * dy < min_dist)
                            break;
                    }
                j = k - 1;
                continue;
            }
            dist = dx * dx + dy * dy;
            if (dist < min_dist)
                min_dist = dist;
        }

    cout << min_dist << '\n';

    delete[] p;

    return 0;
}
