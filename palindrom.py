def get_longest_palindrome(origin: str) -> str:
    longest_palindrome = ""

    for i in range(len(origin)):
        for j in range(i + 1, len(origin) + 1):
            substring = origin[i:j]
            if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                longest_palindrome = substring
    return longest_palindrome

