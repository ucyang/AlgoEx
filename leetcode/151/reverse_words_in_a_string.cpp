class Solution {
public:
    string reverseWords(string s) {
        size_t i, j;

        i = 0;
        for (j = 0; s[j] == ' '; j++) {}

        do
        {
            s[i++] = s[j];
            if (s[j] == ' ')
                for (; s[j] && s[j] == ' '; j++) {}
            else
                j++;
        }
        while (s[j]);

        s.erase(s[i - 1] == ' ' ? i - 1 : i);

        reverse(s.begin(), s.end());

        i = 0;
        for (size_t k = 1;; k++)
        {
            if (!s[k] || s[k] == ' ')
            {
                for (size_t j = k - 1; i < j; i++, j--)
                {
                    auto c = s[i];
                    s[i] = s[j];
                    s[j] = c;
                }
                if (!s[k])
                    break;
                i = k + 1;
            }
        }

        return s;
    }
};
