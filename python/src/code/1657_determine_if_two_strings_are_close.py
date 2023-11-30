"""
1657. 确定两个字符串是否接近
https://leetcode.cn/problems/determine-if-two-strings-are-close
"""


def close_string(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    freq1, freq2 = build_frequency_list(word1), build_frequency_list(word2)
    for f1, f2 in zip(freq1, freq2):
        if (f1 > 0) ^ (f2 > 0):
            return False
    freq1.sort()
    freq2.sort()
    return freq1 == freq2


def build_frequency_list(word: str) -> list[int]:
    frequency = [0] * 26
    for ch in word:
        frequency[ord(ch) - ord("a")] += 1
    return frequency


if __name__ == "__main__":
    assert close_string("abc", "bca")
    assert not close_string("a", "aa")
    assert close_string("cabbba", "abbccc")
    assert not close_string("cabbba", "aabbss")
    assert not close_string("uau", "ssx")
