def check_vowel(s):
    count = 0

    vowel = "aeiouAEIOU"

    for i in s:
        if i in vowel:
            count += 1

    return count

text = "i am niranjan"
z = check_vowel(text)
print(z)