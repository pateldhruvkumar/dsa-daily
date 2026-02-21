import re
def is_palindrome(s) -> bool:
    cleaned_string = re.sub(r'[^a-zA-Z0-9]','', s).lower()
    print("Cleaned string: ", cleaned_string)

    return cleaned_string == cleaned_string[::-1]

s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))