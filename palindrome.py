def is_palindrome(text):
    text = text.replace(" ","").lower()
    return text == text[::-1]

inputt = "saas"
if is_palindrome(inputt):
    print("palindrome")
else:
    print("not palindrome")    


