def  palindrome_string(s):
    revised_string=s[::-1]
    if revised_string == s:
        return "string is  palindrome"
    else:
        return "string is normal"

print( palindrome_string("solos"))
