def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def is_alpha(s):
    return s.isalpha()
