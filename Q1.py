#basic calculater
a=int(input("Enter the first number:-"))
b=int(input("Enter the secound number:-"))
print('''Choose the opration
            Addition -> +
            Subtaction -> -
            Multipication -> *
            Divition -> /''')
Op=input()

if Op=='+':
    print('The addition of given digits',a+b)

elif Op=='-':
    print('The subtraction of given digits',a-b)

elif Op=='*':
    print('The multipication of given digits',a*b)

elif Op=='/':
    print('The divition of given digits',a/b)

else:
    print('invalid entery')