// Reference:
// https://oj.uz/problem/view/CEOI09_tri - Solution of tutis

#include <iostream>
#include <memory>
#include <algorithm>
#include <vector>

using namespace std;

struct P
{
	int x, y;

	const P operator-(const P& rhs) const
	{
		return { x - rhs.x, y - rhs.y };
	}
};

inline long long cross(const P& a, const P& b)
{
	return 1LL * a.x * b.y - 1LL * a.y * b.x;
}

void add(vector<P>& t, const P& a)
{
	while (!t.empty() && cross(a, t.back()) == 0)
		t.pop_back();
	while (t.size() >= 2
		&& cross(a - t.back(), t.back() - t[t.size() - 2]) >= 0)
		t.pop_back();
	t.push_back(a);
}

struct T
{
	vector<P> t;
	shared_ptr<T> left, right;

	T(const vector<P>& a, int i, int j)
	{
		if (i >= j)
		{
			t = { a[i] };
			return;
		}
		left = make_shared<T>(a, i, (i + j) / 2);
		right = make_shared<T>(a, (i + j) / 2 + 1, j);
		t = left->t;
		for (const auto& c : right->t)
			add(t, c);
	}

	bool check(const P& a, const P& b) const
	{
		if (cross(b, t[0]) <= 0 || cross(t.back(), a) <= 0)
			return false;
		if (cross(a, t[0]) <= 0 && cross(t.back(), b) <= 0)
		{
			int l = 0;
			int h = static_cast<int>(t.size() - 1);

			while (l < h)
			{
				int m = (l + h) / 2;
				int n = m + 1;
				long long c1 = cross(b - a, t[m] - a);
				long long c2 = cross(b - a, t[n] - a);

				if (c1 < 0 || c2 < 0)
					return true;
				if (c1 < c2)
					h = m;
				else
					l = n;
			}

			return cross(b - a, t[l] - a) < 0;
		}

		return left->check(a, b) || right->check(a, b);
	}
};

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int k, m;
	cin >> k >> m;

	vector<P> p(k);
	for (auto& e : p)
		cin >> e.x >> e.y;
	sort(p.begin(), p.end(), [](const auto& a, const auto& b) {
		long long t = cross(a, b);
		return (t != 0) ? t < 0 : a.x < b.x;
	});

	T seg(p, 0, k - 1);
	while (m--)
	{
		P a, b;
		cin >> a.x >> a.y >> b.x >> b.y;
		if (cross(a, b) > 0)
			swap(a, b);
		cout << (seg.check(a, b) ? 'Y' : 'N') << '\n';
	}

	return 0;
}