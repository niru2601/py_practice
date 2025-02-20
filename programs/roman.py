import re 

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    pattern = r"^M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"
    N = int(input())
    
    mail = []
    for i in range(0, N):
        z = input()
        mail.append(z)
    # Match the input string against the pattern
    for i in range(0,N):
        if re.match(pattern,mail[i]):
            print('Yes')
        else:
            print('NO')
    return 0

if __name__ == '__main__':
    main()