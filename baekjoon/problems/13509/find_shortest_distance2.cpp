#include <iostream>
#include <algorithm>

using namespace std;

struct Point
{
    long long idx;
    long long x, y;
    long long min_dist;
};

int main()
{
    Point* points = nullptr;
    Point *p, *q;

    long long dx, dy;
    long long dist, dist2;

    long long n;
    long long i, j;

    auto InitMinDist = [&](auto i, auto j) {
        p = points + i;
        q = points + j;
        dx = abs(p->x - q->x);
        dy = abs(p->y - q->y);
        p->min_dist = dx + dy;
    };

    auto InitMinDist2 = [&](auto i) {
        p = points + i;
        q = p - 1;
        dx = abs(p->x - q->x);
        dy = abs(p->y - q->y);
        dist = dx + dy;
        q = p + 1;
        dx = abs(p->x - q->x);
        dy = abs(p->y - q->y);
        dist2 = dx + dy;
        p->min_dist = min(dist, dist2);
    };

    auto UpdateMinDist = [&](auto j) {
        q = points + j;
        dx = abs(p->x - q->x);
        dy = abs(p->y - q->y);
        if (dx >= p->min_dist)
            return true;
        dist = dx + dy;
        if (dist < p->min_dist)
            p->min_dist = dist;
        return false;
    };

    ios::sync_with_stdio(false);

    cin >> n;

    points = new Point[n];
    if (!points)
        return 0x1;

    for (i = 0; i < n; ++i)
    {
        p = points + i;
        p->idx = i;
        cin >> p->x >> p->y;
    }

    sort(points, points + n, [](const auto& p1, const auto& p2) {
        return p1.x < p2.x || (p1.x == p2.x && p1.y < p2.y);
    });
    
    InitMinDist(0, 1);
    for (j = 1; j < n; ++j)
        if (UpdateMinDist(j))
            break;

    for (i = 1; i < n - 1; ++i)
    {
        InitMinDist2(i);
        for (j = i - 1; j >= 0; --j)
            if (UpdateMinDist(j))
                break;
        for (j = i + 1; j < n; ++j)
            if (UpdateMinDist(j))
                break;
    }

    InitMinDist(n - 1, n - 2);
    for (j = n - 2; j >= 0; --j)
        if (UpdateMinDist(j))
            break;

    sort(points, points + n, [](const auto& p1, const auto& p2) {
        return p1.idx < p2.idx;
    });
    
    for (i = 0; i < n; ++i)
        cout << points[i].min_dist << '\n';
    
    delete[] points;

    return 0;
}
