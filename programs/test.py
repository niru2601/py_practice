class voe:
    def __init__(self,vowel):
        self.vowel = vowel

    def check(self):
        count = 0
        pqr = []
        abc = "niranjan"
        for i in range(len(vowel)):
            for j in abc:
                if vowel[i] == j:
                    count += 1
                    pqr.append(j)
        yield pqr
        yield count

vowel = "aeiou"

result = voe
result1 = result.check(vowel)


# To print the result, you need to iterate over the generator:
for item in result1:
    print(item)
