#Voting System
name=input('Enter your name: ')
age=int(input('Enter your age: '))
if age>=18:
    print('You are eligible')
    print('Make a choice')
    print(''' Voting List
      1. BJP
      2. SAPA
      3. SP
      4. NONE''')
    VOTE=int(input())
    if VOTE==1:
        print('Your Vote to BJP was counted')
    if VOTE==2:
        print('Your Vote to sapa was counted')
    if VOTE==3:
        print('Your Vote to sp was counted')
    if VOTE==4:
        print('Your Vote to none was counted')
    elif VOTE>=5:
        print('invalid choice')
else:
    print('you are not eligible')