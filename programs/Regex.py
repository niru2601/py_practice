import re


# #fUNC PRACTICE
# def main():
#     txt = "The quick brown fox jumps over the lazy dog"
    
#     # print the list of 'o' present in the string txt
#     x = re.findall("o",txt)
#     print(x)
#     # print the index of first occurrence of 'h' in the string txt using search function
#     y = re.search("h",txt)
#     print(y.start())
#     a = txt[::-1]
#     print(a)
#     b = re.search('h',a)
#     print(b.start())
#     # convert the first 3 white-space character into '#' and print the changed txt
#     z = re.sub("\s","#",txt,3)
#     print(z)
    
#     return 0

# if __name__ == '__main__':
#     main()


# #mobile validation 

# import re
# def main():
#     # YOUR CODE GOES HERE
#     # Please take input and print output to standard input/output (stdin/stdout)
#     # E.g. 'input()/raw_input()' for input & 'print' for output
#     number = int(input())
#     b=[]
#     for i in range (0,number):
#         c = input()
#         b.append(c)
    
#     for i in range(0,number):
#         if re.match(r"^[6-9]\d{9}$",b[i]):
#             print("YES")
#         else:
#             print("NO")
    
#     return 0

# if __name__ == '__main__':
#     main()



# #Email validation 

# import re

# def email():
#     N = int(input())
    
#     mail = []
#     for i in range(0, N):
#         z = input()
#         mail.append(z)
    
#     pattern = r"^[a-zA-Z0-9-_]+@[A-Za-z0-9]+\.[A-Za-z]{2,3}$"
#     new_mail = list(filter(lambda x : re.match(pattern,x),mail))
#     print(sorted(new_mail))

        
# email()    


z1 = re.findall("[aeiou]","hi, i am niranjan patil",re.IGNORECASE)
print(z1)

print(len(z1))