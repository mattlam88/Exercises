
def is_palindrome(string):
    if len(string) <= 1:
        return True
    else:
        return string == string[::-1]
