#include <iostream>
#include <complex>
#include <vector>
#include <numeric>

using namespace std;

using base = complex<double>;

void fft(vector<base>& a, bool inv)
{
    const size_t n = a.size();
    const double ang = 2 * M_PI / n * (inv ? 1 : -1);
    size_t bit, i, j, k;
    vector<base> roots(n >> 1);
    base t;

    for (i = 1, j = 0; i < n; ++i)
    {
        for (bit = n >> 1; !((j ^= bit) & bit); bit >>= 1);
        if (i < j)
            swap(a[i], a[j]);
    }

    for (i = 0; i < n >> 1; ++i)
        roots[i] = base(cos(ang * i), sin(ang * i));

    for (i = 1; i < n; i <<= 1)
        for (j = 0; j < n; j += i << 1)
            for (k = 0; k < i; ++k)
            {
                t = a[i + j + k] * roots[n / (i << 1) * k];
                a[i + j + k] = a[j + k] - t;
                a[j + k] += t;
            }

    if (inv)
        for (i = 0; i < n; i++)
            a[i] /= n;
}

void multiply(vector<unsigned long long>& v,
        const vector<unsigned long long>& w)
{
    size_t n, i, j;
    unsigned long long av, bv, cv;
    base ans1, ans2, ans3, ans4;

    for (n = 2; n < v.size() + w.size(); n <<= 1);

    vector<base> v1(n), v2(n), r1(n), r2(n);

    for (i = 0; i < v.size(); ++i)
        v1[i] = base(v[i] >> 15, v[i] & 0x7fff);
    for (i = 0; i < w.size(); ++i)
        v2[i] = base(w[i] >> 15, w[i] & 0x7fff);

    fft(v1, false);
    fft(v2, false);

    for (i = 0; i < n; ++i)
    {
        j = i ? n - i : i;
        ans1 = (v1[i] + conj(v1[j])) * base(0.5, 0);
        ans2 = (v1[i] - conj(v1[j])) * base(0, -0.5);
        ans3 = (v2[i] + conj(v2[j])) * base(0.5, 0);
        ans4 = (v2[i] - conj(v2[j])) * base(0, -0.5);
        r1[i] = (ans1 * ans3) + (ans1 * ans4) * base(0, 1);
        r2[i] = (ans2 * ans3) + (ans2 * ans4) * base(0, 1);
    }

    fft(r1, true);
    fft(r2, true);

    v.resize(n);
    for (i = 0; i < n; ++i)
    {
        av = llround(r1[i].real());
        bv = llround(r1[i].imag()) + llround(r2[i].real());
        cv = llround(r2[i].imag());
        v[i] = (av << 30) + (bv << 15) + cv;
    }
}

int main()
{
    unsigned long long n, m, i;
    vector<unsigned long long> f, g;

    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m;

    f.resize(n + 1);
    g.resize(m + 1);

    for (i = 0; i <= n; ++i)
        cin >> f[i];
    for (i = 0; i <= m; ++i)
        cin >> g[i];

    multiply(f, g);

    cout << accumulate(f.cbegin(), f.cend(), 0ULL,
            bit_xor<unsigned long long>()) << '\n';

    return 0;
}
