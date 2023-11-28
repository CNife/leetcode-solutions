def repeated_substring_pattern(s: str) -> bool:
    return len(s) >= 2 and s in (s * 2)[1:-1]


if __name__ == "__main__":
    assert repeated_substring_pattern("abab")
    assert not repeated_substring_pattern("aba")
    assert repeated_substring_pattern("abcabcabcabc")
