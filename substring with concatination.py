class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_count, string_length = len(words), len(s)

        char_count = words_count * len(words[0])
        word_dict = {}
        res = []
        for j in words:
            if j in word_dict:
                word_dict[j] += 1
            else:
                word_dict[j] = 1

        for k in range(0, (string_length - char_count + 1), 1):
            temp_dict = word_dict.copy()
            j = k
            count = words_count

            while j < k + char_count:
                wd = s[j : j + len(words[0]) :]

                if wd not in word_dict or temp_dict[wd] == 0:
                    break
                else:
                    temp_dict[wd] -= 1
                    count -= 1
                    j += len(words[0])
            if count == 0:
                res.append(k)
        return res
