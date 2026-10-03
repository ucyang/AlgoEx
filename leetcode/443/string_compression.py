class Solution:
    def compress(self, chars: list[str]) -> int:
        last_c = chars[0]
        last_idx = 0
        count = 0

        for c in chars:
            if c == last_c:
                count += 1
            else:
                last_idx = self.compress_last_char(chars, last_c, last_idx, count)

                last_c = c
                count = 1
        else:
            last_idx = self.compress_last_char(chars, last_c, last_idx, count)

        return last_idx


    def compress_last_char(self, chars: list[str], last_c: str, last_idx: int,
                           count: int) -> int:
        chars[last_idx] = last_c
        last_idx += 1

        if count > 1:
            count_str = str(count)
            count_str_len = len(count_str)

            chars[last_idx:last_idx + count_str_len] = count_str
            last_idx += count_str_len

        return last_idx
