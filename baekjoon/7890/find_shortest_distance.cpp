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

    long long tn, n, max_n = 0;
    long long i, j;

    ios::sync_with_stdio(false);

    cin >> tn;

    while (tn--)
    {
        cin >> n;
    
        if (n > max_n)
        {
            delete[] points;
            points = new Point[n];
            if (!points)
                return 0x1;
            max_n = n;
        }
    
        for (i = 0; i < n; ++i)
        {
            p = points + i;
            p->idx = i;
            cin >> p->x >> p->y;
        }
    
        sort(points, points + n, [](const auto& p1, const auto& p2) {
            return p1.x < p2.x || (p1.x == p2.x && p1.y < p2.y);
        });
        
        p = points;
        q = p + 1;
        dx = p->x - q->x;
        dy = p->y - q->y;
        p->min_dist = dx * dx + dy * dy;
        
        for (j = 1; j < n; ++j)
        {
            q = points + j;
            dx = p->x - q->x;
            dy = p->y - q->y;
            dx *= dx;
            dy *= dy;
            if (dx >= p->min_dist)
                break;
            dist = dx + dy;
            if (dist < p->min_dist)
                p->min_dist = dist;
        }

        for (i = 1; i < n - 1; ++i)
        {
            p = points + i;

            q = p - 1;
            dx = p->x - q->x;
            dy = p->y - q->y;
            dist = dx * dx + dy * dy;

            q = p + 1;
            dx = p->x - q->x;
            dy = p->y - q->y;
            dist2 = dx * dx + dy * dy;

            p->min_dist = min(dist, dist2);

            for (j = i - 1; j >= 0; --j)
            {
                q = points + j;
                dx = p->x - q->x;
                dy = p->y - q->y;
                dx *= dx;
                dy *= dy;
                if (dx >= p->min_dist)
                    break;
                dist = dx + dy;
                if (dist < p->min_dist)
                    p->min_dist = dist;
            }

            for (j = i + 1; j < n; ++j)
            {
                q = points + j;
                dx = p->x - q->x;
                dy = p->y - q->y;
                dx *= dx;
                dy *= dy;
                if (dx >= p->min_dist)
                    break;
                dist = dx + dy;
                if (dist < p->min_dist)
                    p->min_dist = dist;
            }
        }

        p = points + n - 1;
        q = p - 1;
        dx = p->x - q->x;
        dy = p->y - q->y;
        p->min_dist = dx * dx + dy * dy;
        
        for (j = n - 2; j >= 0; --j)
        {
            q = points + j;
            dx = p->x - q->x;
            dy = p->y - q->y;
            dx *= dx;
            dy *= dy;
            if (dx >= p->min_dist)
                break;
            dist = dx + dy;
            if (dist < p->min_dist)
                p->min_dist = dist;
        }
    
        sort(points, points + n, [](const auto& p1, const auto& p2) {
            return p1.idx < p2.idx;
        });
        
        for (i = 0; i < n; ++i)
            cout << points[i].min_dist << '\n';
    }
    
    delete[] points;

    return 0;
}
