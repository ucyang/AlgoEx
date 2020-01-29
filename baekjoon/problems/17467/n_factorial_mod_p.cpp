// Reference: https://www.secmem.org/blog/2019/09/17/fast-factorial-calculation/

#include <iostream>
#include <complex>
#include <vector>
#include <algorithm>

using namespace std;

unsigned long long power_mod(unsigned long long x, unsigned long long y,
        unsigned long long p)
{
    unsigned long long result = 1;

    x %= p;
    y %= p;

    while (y > 0)
    {
        if (y & 1)
            result = static_cast<unsigned __int128>(result) * x % p;
        y >>= 1;
        x = static_cast<unsigned __int128>(x) * x % p;
    }

    return result;
}

inline unsigned long long mod_inverse(unsigned long long x,
        unsigned long long p)
{
    return (__gcd(x, p) == 1) ? power_mod(x, p - 2, p) : 0;
}

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
        const vector<unsigned long long>& w, unsigned long long p)
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
        av = llround(r1[i].real()) % p;
        bv = llround(r1[i].imag()) % p + llround(r2[i].real()) % p;
        cv = llround(r2[i].imag()) % p;
        v[i] = ((av << 30) + (bv << 15) + cv) % p;
    }
}

void lagrange(vector<unsigned long long>& h, unsigned long long p)
{
    const size_t d = h.size() - 1;
    size_t i;
    vector<unsigned long long> fact(4 * d + 2),
        fact_inv(4 * d + 2), inv(4 * d + 2);
    vector<unsigned long long> f(d + 1), g(4 * d + 2);

    fact[0] = 1;
    for (i = 1; i < 4 * d + 2; ++i)
        fact[i] = i * fact[i - 1] % p;

    fact_inv[4 * d + 1] = mod_inverse(fact[4 * d + 1], p);
    for (i = 4 * d + 1; i > 0; --i)
        fact_inv[i - 1] = fact_inv[i] * i % p;

    for (i = 1; i < 4 * d + 2; ++i)
        inv[i] = fact[i - 1] * fact_inv[i] % p;

    for (i = 0; i <= d; ++i)
    {
        f[i] = (h[i] * fact_inv[i] % p) * fact_inv[d - i] % p;
        if ((d - i) % 2 && f[i])
            f[i] = p - f[i];
    }

    g[d + 1] = 1;
    for (i = 0; i <= d; ++i)
        g[d + 1] = g[d + 1] * (d + 1 - i) % p;
    for (i = d + 2; i < 4 * d + 2; ++i)
        g[i] = g[i - 1] * (i * inv[i - d - 1] % p) % p;

    multiply(f, inv, p);

    h.resize(4 * d + 2);
    for (i = d + 1; i < 4 * d + 2; ++i)
        h[i] = f[i] * g[i] % p;
}

void squarepoly(vector<unsigned long long>& poly, unsigned long long p)
{
    size_t len, i;

    lagrange(poly, p);
    len = poly.size() / 2;

    for (i = 0; i < len; ++i)
        poly[i] = poly[2 * i] * poly[2 * i + 1] % p;

    poly.resize(len);
}

int main()
{
    unsigned long long n, p, result = 1;
    unsigned long long d, m, i;
    vector<unsigned long long> fact_part{ 1, 2 };

    cin >> n >> p;

    if (!p)
    {
        cout << n << '\n';
        return 0;
    }

    if (p == 1 || n >= p)
    {
        cout << 0 << '\n';
        return 0;
    }

    if (p < 100000)
    {
        for (i = 2; i <= n; ++i)
            result = result * i % p;
        cout << result << '\n';
        return 0;
    }

    for (d = 1; d * (d + 1) < n; d <<= 1)
        squarepoly(fact_part, p);

    m = n / d;

    for (i = 0; i < m; ++i)
        result = result * fact_part[i] % p;
    for (i = m * d + 1; i <= n; ++i)
        result = result * i % p;

    cout << result << '\n';

    return 0;
}
