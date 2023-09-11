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