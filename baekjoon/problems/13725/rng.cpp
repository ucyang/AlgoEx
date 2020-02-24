// References:
// https://www.codechef.com/problems/RNG - Solutions of ryuhei, theguiler
// https://discuss.codechef.com/t/rng-editorial/10068

#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>

using namespace std;
using namespace placeholders;

constexpr size_t P = 104857601, R = 3, K = 16, M = 1 << K;

size_t A[M], C[M];
size_t w[M >> 1], y[M >> 1], v[M >> 1];

inline size_t add(size_t a, size_t b)
{
    size_t c = a + b;
    return c >= P ? c - P : c;
}

inline size_t sub(size_t a, size_t b)
{
    return a >= b ? a - b : a + P - b;
}

inline size_t mul(size_t a, size_t b)
{
    return a * b % P;
}

inline size_t fpow(size_t a, size_t n)
{
    size_t ret = 1;

    for (; n; n >>= 1)
    {
        if (n & 1)
            ret = mul(ret, a);
        a = mul(a, a);
    }

    return ret;
}

inline size_t inv(size_t a)
{
    return fpow(a, P - 2);
}

void genwy(size_t i, size_t b, size_t z, size_t x)
{
    if (b)
    {
        genwy(i, b >> 1, z, x);
        genwy(i | b, b >> 1, mul(z, w[b]), mul(x, y[b]));
    }
    w[i] = z;
    y[i] = x;
}

void fft(size_t* a, size_t k, bool inv)
{
    if (!inv)
    {
        const size_t m = 1 << k;
        size_t u = 1, v = m >> 1;

        for (size_t i = k; i > 0; --i)
        {
            for (size_t jh = 0; jh < u; ++jh)
            {
                size_t wj = w[jh];
                for (size_t j = jh << i, je = j + v; j < je; ++j)
                {
                    size_t Ajv = mul(wj, a[j + v]);
                    a[j + v] = sub(a[j], Ajv);
                    a[j] = add(a[j], Ajv);
                }
            }
            u <<= 1;
            v >>= 1;
        }
    }
    else
    {
        const size_t m = 1 << k;
        size_t u = m >> 1, v = 1;
        for (size_t i = 1; i <= k; ++i)
        {
            for (size_t jh = 0; jh < u; ++jh)
            {
                size_t wj = y[jh];
                for (size_t j = jh << i, je = j + v; j < je; j++)
                {
                    size_t Ajv = sub(a[j], a[j + v]);
                    a[j] = add(a[j], a[j + v]);
                    a[j + v] = mul(wj, Ajv);
                }
            }
            u >>= 1;
            v <<= 1;
        }
    }
}

size_t solve(const vector<size_t>& a, const vector<size_t>& c, size_t n)
{
    const size_t k = a.size();
    size_t i;

    copy(a.cbegin(), a.cbegin() + k, A);
    transform(c.cbegin(), c.cbegin() + k, C + 1, bind(sub, 0, _1));
    C[0] = 1;

    size_t z = fpow(R, P >> K);
    size_t x = inv(z);
    for (i = M >> 2; i; i >>= 1)
    {
        w[i] = z;
        y[i] = x;
        z = mul(z, z);
        x = mul(x, x);
    }
    genwy(0, M >> 2, 1, 1);

    fft(A, K, false);
    fft(C, K, false);

    transform(A, A + M, C, A, mul);

    fft(A, K, true);
    fill(A + k, A + M, 0);
    fft(A, K, false);

    const size_t im = inv(M);
    const size_t im2 = inv(M >> 1);
    size_t ima = im, imc = 1;

    z = fpow(R, P >> K);
    size_t wi = im2;
    for (i = 0; i < M >> 1; ++i)
    {
        v[i] = wi;
        wi = mul(wi, z);
    }

    for (;; n >>= 1)
    {
        for (i = 0; i < M; ++i)
            A[i] = mul(A[i], C[i ^ 1]);

        for (i = 0; i < M >> 1; ++i)
            A[i] = (n & 1) ? mul(y[i], sub(A[i << 1], A[(i << 1) + 1]))
                    : add(A[i << 1], A[(i << 1) + 1]);

        ima = mul(ima, imc);
        if (n == 1)
        {
            fft(A, K - 1, true);
            ima = mul(ima, im);
            break;
        }

        copy(A, A + (M >> 1), A + (M >> 1));
        fft(A + (M >> 1), K - 1, true);
        for (i = 0; i < M >> 1; ++i)
            A[i + (M >> 1)] = mul(v[i], A[i + (M >> 1)]);
        fft(A + (M >> 1), K - 1, false);
        ima = ((ima & 1) ? P + ima : ima) >> 1;

        for (i = 0; i < M >> 1; ++i)
            C[i] = mul(C[i << 1], C[(i << 1) + 1]);

        copy(C, C + (M >> 1), C + (M >> 1));
        fft(C + (M >> 1), K - 1, true);
        for (i = 0; i < M >> 1; ++i)
            C[i + (M >> 1)] = mul(v[i], C[i + (M >> 1)]);
        fft(C + (M >> 1), K - 1, false);
        imc = mul(imc, imc);
    }

    return mul(A[0], ima);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    size_t k, n;
    cin >> k >> n;

    vector<size_t> a(k), c(k);
    for (auto& e : a)
        cin >> e;
    for (auto& e : c)
        cin >> e;

    cout << solve(a, c, n - 1) << '\n';

    return 0;
}
