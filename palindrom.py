<<<<<<< HEAD
from typing import Union
user_input = input("Add string and number: ")
def is_palindrome(origin: Union[str, int]) -> bool:
    origin = str(origin)
    length = len(origin)
    for i in range(length // 2):
        if origin[i] != origin[length - 1 - i]:
            return False
    return  True
result = is_palindrome(user_input)
if result:
    print(f"{user_input} - Is pal.")
else:
    print(f"{user_input} - Is not pal.")

    
def get_longest_palindrome(origin: str) -> str:
    longest_palindrome = ""

    for i in range(len(origin)):
        for j in range(i + 1, len(origin) + 1):
            substring = origin[i:j]
            if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                longest_palindrome = substring
    return longest_palindrome
input_str1 = "0123219"
input_str2 = "1012210"
result1 = get_longest_palindrome(input_str1)
result2 = get_longest_palindrome(input_str2)
print("The longest palindrom for '0123219':", result1)
print("THe longest palindrom for  '1012210':", result2
>>>>>>> get_longest_palindrome
