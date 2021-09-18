#include <iostream>
#include <vector>
#include <set>

using namespace std;

struct Point
{
    long long x, y, z;

    Point(long long ax, long long ay, long long az) : x(ax), y(ay), z(az) {}

    bool operator<(const Point& other) const
    {
        return x < other.x || (x == other.x
                && (y < other.y || (y == other.y && z < other.z)));
    }
};

int main()
{
    set<Point> s;
    vector<Point> v;
    long long x, y, z;
    long long dx, dy, dz;
    long long dist;
    long long min_dist;
    long long min_count = 0;
    long long n;
    long long i, j;

    ios::sync_with_stdio(false);

    cin >> n;

    for (i = 0; i < n; ++i)
    {
        cin >> x >> y >> z;
        s.emplace(x, y, z);
    }

    v.assign(s.cbegin(), s.cend());
    n = v.size();

    dx = v[0].x - v[1].x;
    dy = v[0].y - v[1].y;
    dz = v[0].z - v[1].z;
    min_dist = dx * dx + dy * dy + dz * dz;

    for (i = 0; i < n; ++i)
        for (j = i + 1; j < n; ++j)
        {
            dx = v[i].x - v[j].x;
            dy = v[i].y - v[j].y;
            dz = v[i].z - v[j].z;
            dx *= dx;
            dy *= dy;
            dz *= dz;
            if (dx > min_dist)
                break;
            if (dy > min_dist || dz > min_dist)
                continue;
            dist = dx + dy + dz;
            if (dist < min_dist)
            {
                min_dist = dist;
                min_count = 1;
            }
            else if (dist == min_dist)
                ++min_count;
        }

    cout << min_dist << endl << min_count << endl;

    return 0;
}
