import re
def is_palindrome(s) -> bool:

    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    left,right = 0, len(cleaned_string) - 1

    while left < right:
        if cleaned_string[left] == cleaned_string[right]:
            left += 1
            right -= 1
        else:
            skip_left = cleaned_string[left + 1 :  right + 1]
            skip_right = cleaned_string [left : right + 1]

            return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
    return True

s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))