def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    
    mail = []
    for i in range(0, N):
        x, y = input().split()
# Convert to the desired types (e.g., integers)
          
        mail.append((x, y))
        
    
    for i in range(0,N):
        try:
            x,y = mail[i]
            x = int(x)
            y = int(y)
            z = x//y
            print(z)
        except ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")
        except ValueError as e:
            print("Error Code:", e)
    return 0

if __name__ == '__main__':
    main()