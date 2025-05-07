def lengthOfLastWord(s: str) -> int:
    words = s.strip().split()
    return len(words[-1])
print(lengthOfLastWord("hello world"))