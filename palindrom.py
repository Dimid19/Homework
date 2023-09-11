from typing import Union
user_input = input("Add string and number: ")
def is_palindrome(origin: Union[str, int]) -> bool:
    origin = str(origin)
    length = len(origin)
